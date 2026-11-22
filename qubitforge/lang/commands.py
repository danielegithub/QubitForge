"""Comandi del linguaggio. I nomi sono in inglese; gli alias stanno nei file di lingua."""
import difflib
from pathlib import Path

from .. import i18n
from ..core.circuit import Instruction
from ..core.errors import QFError
from ..core.gates import GATES
from ..core.machine import MAX_QUBITS
from ..learn import content
from ..terminal import render, theme
from .expr import eval_angle
from .session import QuitShell, Session

t = i18n.t
MAX_SHOTS = 200_000
MAX_DEPTH = 3
# L'ordine delle categorie è quello mostrato da help.
HELP_GROUPS = {
    "machine": ("qreg [n]", "reset", "undo"),
    "gates": tuple(gate.usage for gate in GATES.values()),
    "analysis": ("state", "probs", "bloch [q]", "circuit", "qasm"),
    "measure": ("measure [q|all]", "run [shots]"),
    "files": ("save <file.qf>", "load <file.qf>"),
    "learn": ("lesson [n]", "example [name]", "explain [on|off]", "help [command]"),
    "system": ("lang [code]", "clear", "quit"),
}
USAGE = {}
for usages in HELP_GROUPS.values():
    for usage in usages:
        USAGE[usage.split()[0]] = usage


def execute_line(session: Session, line: str):
    words = line.partition("#")[0].split()
    if not words:
        return
    word, *args = words
    word = word.lower()
    name = resolve(word)
    if name is None:
        message = t("err.unknown_command", cmd=word)
        names = [*USAGE, *i18n.aliases()]
        matches = difflib.get_close_matches(word, names, n=1, cutoff=0.6)
        if matches:
            message += " " + t("err.did_you_mean", s=matches[0])
        session.out(theme.err(message + " " + t("err.try_help")))
        return
    try:
        run_command(session, name, args)
    except QFError as error:
        session.out(theme.err(t(error.key, **error.params)))


def resolve(word):
    if word in USAGE:
        return word
    return i18n.aliases().get(word)


def run_command(session, name, args):
    machine = session.machine
    if name in GATES:
        apply_gate(session, GATES[name], args)
        return

    match name:
        case "qreg":
            if args:
                machine.reset(parse_integer(args[0]))
                session.out(t("qreg.created", n=machine.n, last=machine.n - 1))
            else:
                session.out(t("qreg.info", n=machine.n, last=machine.n - 1, max=MAX_QUBITS))
        case "reset":
            machine.reset()
            session.out(t("reset.done"))
        case "undo":
            undone = machine.undo()
            session.out(t("undo.done" if undone else "undo.nothing"))
        case "state":
            session.out(render.state(machine))
        case "probs":
            session.out(render.probs(machine))
        case "bloch":
            for qubit in parse_qubits(session, args) or range(machine.n):
                session.out(render.bloch_report(machine, qubit))
        case "circuit":
            session.out(render.circuit(machine.circuit, machine.n))
        case "qasm":
            session.out(machine.circuit.to_qasm(machine.n).rstrip())
        case "measure":
            measure(session, args)
        case "run":
            shots = parse_integer(args[0]) if args else 1024
            if not 1 <= shots <= MAX_SHOTS:
                raise QFError("err.shots_range", max=MAX_SHOTS)
            session.out(render.counts(machine.sample(shots), shots))
        case "save":
            save_circuit(session, args)
        case "load":
            load_script(session, args)
        case "lesson":
            show_lesson(session, args)
        case "example":
            run_example(session, args)
        case "explain":
            if args and args[0].lower() in ("on", "off"):
                session.explain = args[0].lower() == "on"
            else:
                session.explain = not session.explain
            session.out(t("explain.on" if session.explain else "explain.off"))
        case "help":
            show_help(session, args)
        case "lang":
            select_language(session, args)
        case "clear":
            session.out("\033[2J\033[H" if theme.enabled else "\n" * 3)
        case "quit":
            session.out(t("quit.bye"))
            raise QuitShell


def parse_qubits(session, tokens):
    """Converte "0", "q1" o "all" in indici, controllando che esistano."""
    n = session.machine.n
    out = []
    for tok in tokens:
        tok = tok.lower()
        if tok == "all":
            out.extend(range(n))
            continue
        try:
            q = int(tok.removeprefix("q"))
        except ValueError:
            raise QFError("err.bad_qubit", token=tok) from None
        if not 0 <= q < n:
            raise QFError("err.qubit_range", q=q, last=n - 1)
        out.append(q)
    return out


def parse_integer(text):
    try:
        return int(text)
    except ValueError:
        raise QFError("err.bad_int", text=text) from None


def apply_gate(session, gate, args):
    if len(args) < gate.params + 1:
        raise QFError("err.arity", usage=gate.usage)
    angles = tuple(eval_angle(text) for text in args[:gate.params])
    qubits = parse_qubits(session, args[gate.params:])
    if gate.arity == 1:
        # "h all" esegue una H separata su ciascun qubit.
        for qubit in qubits:
            session.machine.execute(Instruction(gate.name, (qubit,), angles))
    else:
        session.machine.execute(Instruction(gate.name, tuple(qubits), angles))
    if session.explain:
        session.out(theme.c("dim", "  ↳ " + t(f"gate.{gate.name}")))


def measure(session, args):
    qubits = parse_qubits(session, args) or range(session.machine.n)
    bits = {}
    for q in qubits:
        p1 = session.machine.sv.prob_one(q)
        bits[q] = session.machine.execute(Instruction("measure", (q,)))
        session.out(t("measure.result", q=q, bit=bits[q], p=p1 * 100))
    if len(qubits) > 1:
        word = "".join(str(bits[q]) for q in sorted(bits, reverse=True))
        session.out(t("measure.all", word=word))


def save_circuit(session, args):
    if not args:
        raise QFError("err.arity", usage="save <file.qf>")
    path = Path(args[0])
    if not path.suffix:
        path = path.with_suffix(".qf")
    if path.exists():
        raise QFError("err.exists", path=str(path))
    try:
        path.write_text(session.machine.circuit.to_script(session.machine.n), encoding="utf-8")
    except OSError as e:
        raise QFError("err.file", path=str(path), reason=e.strerror) from None
    session.out(t("save.done", path=str(path)))


def load_script(session, args):
    if not args:
        raise QFError("err.arity", usage="load <file.qf>")
    path = Path(args[0])
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise QFError("err.file", path=str(path), reason=e.strerror) from None
    run_script(session, lines)
    session.out(t("load.done", path=str(path)))


def run_script(session, lines):
    if session.depth >= MAX_DEPTH:
        raise QFError("err.depth")
    session.depth += 1
    try:
        for raw in lines:
            line = raw.partition("#")[0].strip()
            if line:
                session.out(theme.c("dim", "qf> " + line))
                execute_line(session, line)
    finally:
        session.depth -= 1


def show_lesson(session, args):
    lang = i18n.current()
    if not args:
        session.out(theme.c("bold", t("lesson.list_header")))
        for num, title in content.lessons(lang):
            session.out(f"  {theme.c('cyan', str(num))}  {title}")
        session.out(theme.c("dim", t("lesson.hint")))
        return
    found = content.lesson(lang, parse_integer(args[0]))
    if found is None:
        raise QFError("err.no_lesson", n=args[0])
    title, body = found
    session.out(theme.c("bold yellow", f"━━ {title} ━━"))
    session.out(body)


def run_example(session, args):
    if not args:
        session.out(theme.c("bold", t("example.list_header")))
        for name in content.example_names():
            session.out(f"  {theme.c('cyan', f'{name:<11}')} {t('example.' + name)}")
        session.out(theme.c("dim", t("example.hint")))
        return
    name = args[0].lower()
    lines = content.example_lines(name)
    if lines is None:
        raise QFError("err.unknown_example", name=args[0])
    session.out(theme.c("bold", t("example.running", desc=t("example." + name))))
    run_script(session, lines)
    session.out(render.circuit(session.machine.circuit, session.machine.n))


def show_help(session, args):
    if args:
        name = resolve(args[0].lower())
        if name is None:
            raise QFError("err.unknown_command", cmd=args[0])
        key = f"gate.{name}" if name in GATES else f"cmd.{name}"
        session.out(f"{theme.c('cyan', USAGE[name])}\n  {t(key)}")
        return
    session.out(theme.c("bold yellow", t("help.title")))
    for cat, usages in HELP_GROUPS.items():
        session.out("\n" + theme.c("bold", t(f"cat.{cat}")))
        if cat == "gates":
            for kind in ("single", "rotation", "controlled", "swap"):
                names = " ".join(g.name for g in GATES.values() if g.kind == kind)
                session.out(f"  {theme.c('cyan', names)}   {theme.c('dim', t('gates.' + kind))}")
            continue
        for usage in usages:
            name = usage.split()[0]
            label = theme.c("cyan", f"{usage:<18}")
            session.out(f"  {label} {t('cmd.' + name)}")
    session.out("\n" + theme.c("dim", t("help.more")))


def select_language(session, args):
    langs = i18n.available()
    if not args:
        session.out(t("lang.current", code=i18n.current()))
        for code, name in langs.items():
            session.out(f"  {theme.c('cyan', code)}  {name}")
        return
    if not i18n.set_language(args[0]):
        raise QFError("err.unknown_lang", code=args[0], langs=", ".join(langs))
    session.out(t("lang.set", name=langs[i18n.current()]))
