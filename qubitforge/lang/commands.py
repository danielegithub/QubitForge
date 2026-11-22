"""Comandi del linguaggio. I nomi sono in inglese; gli alias stanno nei file di lingua."""
import difflib
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

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
CATEGORIES = ["machine", "gates", "analysis", "measure", "files", "learn", "system"]


@dataclass
class Command:
    name: str
    usage: str
    category: str
    func: Callable[[Session, list[str]], None]


REGISTRY: dict[str, Command] = {}


def command(name, usage=None, category="system"):
    def register(fn):
        REGISTRY[name] = Command(name, usage or name, category, fn)
        return fn
    return register


def _qubits(s, tokens):
    """Converte "0", "q1" o "all" in indici, controllando che esistano."""
    n = s.machine.n
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


def _int(text):
    try:
        return int(text)
    except ValueError:
        raise QFError("err.bad_int", text=text) from None


def resolve(word):
    return word if word in REGISTRY else i18n.aliases().get(word)


def _gate_command(spec):
    def run(s, args):
        if len(args) < spec.params + 1:
            raise QFError("err.arity", usage=spec.usage)
        params = tuple(eval_angle(a) for a in args[:spec.params])
        qubits = _qubits(s, args[spec.params:])
        if spec.arity == 1:
            groups = [(q,) for q in qubits]       # "h 0 1 2" o "h all"
        else:
            groups = [tuple(qubits)]
        for g in groups:
            s.machine.execute(Instruction(spec.name, g, params))
        if s.explain:
            s.out(theme.c("dim", "  ↳ " + t(f"gate.{spec.name}")))
    return run


for spec in GATES.values():
    REGISTRY[spec.name] = Command(spec.name, spec.usage, "gates", _gate_command(spec))


@command("qreg", "qreg [n]", "machine")
def cmd_qreg(s, args):
    if not args:
        s.out(t("qreg.info", n=s.machine.n, last=s.machine.n - 1, max=MAX_QUBITS))
        return
    s.machine.reset(_int(args[0]))
    s.out(t("qreg.created", n=s.machine.n, last=s.machine.n - 1))


@command("reset", category="machine")
def cmd_reset(s, args):
    s.machine.reset()
    s.out(t("reset.done"))


@command("undo", category="machine")
def cmd_undo(s, args):
    s.out(t("undo.done") if s.machine.undo() else t("undo.nothing"))


@command("state", category="analysis")
def cmd_state(s, args):
    s.out(render.state(s.machine))


@command("probs", category="analysis")
def cmd_probs(s, args):
    s.out(render.probs(s.machine))


@command("bloch", "bloch [q]", "analysis")
def cmd_bloch(s, args):
    for q in _qubits(s, args) or range(s.machine.n):
        s.out(render.bloch_report(s.machine, q))


@command("circuit", category="analysis")
def cmd_circuit(s, args):
    s.out(render.circuit(s.machine.circuit, s.machine.n))


@command("qasm", category="analysis")
def cmd_qasm(s, args):
    s.out(s.machine.circuit.to_qasm(s.machine.n).rstrip())


@command("measure", "measure [q|all]", "measure")
def cmd_measure(s, args):
    qubits = _qubits(s, args) or range(s.machine.n)
    bits = {}
    for q in qubits:
        p1 = s.machine.sv.prob_one(q)
        bits[q] = s.machine.execute(Instruction("measure", (q,)))
        s.out(t("measure.result", q=q, bit=bits[q], p=p1 * 100))
    if len(qubits) > 1:
        word = "".join(str(bits[q]) for q in sorted(bits, reverse=True))
        s.out(t("measure.all", word=word))


@command("run", "run [shots]", "measure")
def cmd_run(s, args):
    shots = _int(args[0]) if args else 1024
    if not 1 <= shots <= MAX_SHOTS:
        raise QFError("err.shots_range", max=MAX_SHOTS)
    s.out(render.counts(s.machine.sample(shots), shots))


@command("save", "save <file.qf>", "files")
def cmd_save(s, args):
    if not args:
        raise QFError("err.arity", usage="save <file.qf>")
    path = Path(args[0])
    if not path.suffix:
        path = path.with_suffix(".qf")
    if path.exists():
        raise QFError("err.exists", path=str(path))
    try:
        path.write_text(s.machine.circuit.to_script(s.machine.n), encoding="utf-8")
    except OSError as e:
        raise QFError("err.file", path=str(path), reason=e.strerror) from None
    s.out(t("save.done", path=str(path)))


@command("load", "load <file.qf>", "files")
def cmd_load(s, args):
    if not args:
        raise QFError("err.arity", usage="load <file.qf>")
    path = Path(args[0])
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as e:
        raise QFError("err.file", path=str(path), reason=e.strerror) from None
    run_script(s, lines)
    s.out(t("load.done", path=str(path)))


def run_script(s, lines):
    if s.depth >= MAX_DEPTH:
        raise QFError("err.depth")
    s.depth += 1
    try:
        for raw in lines:
            line = raw.split("#")[0].strip()
            if line:
                s.out(theme.c("dim", "qf> " + line))
                execute_line(s, line)
    finally:
        s.depth -= 1


@command("lesson", "lesson [n]", "learn")
def cmd_lesson(s, args):
    lang = i18n.current()
    if not args:
        s.out(theme.c("bold", t("lesson.list_header")))
        for num, title in content.lessons(lang):
            s.out(f"  {theme.c('cyan', str(num))}  {title}")
        s.out(theme.c("dim", t("lesson.hint")))
        return
    found = content.lesson(lang, _int(args[0]))
    if found is None:
        raise QFError("err.no_lesson", n=args[0])
    title, body = found
    s.out(theme.c("bold yellow", f"━━ {title} ━━"))
    s.out(body)


@command("example", "example [name]", "learn")
def cmd_example(s, args):
    if not args:
        s.out(theme.c("bold", t("example.list_header")))
        for name in content.example_names():
            s.out(f"  {theme.c('cyan', f'{name:<11}')} {t('example.' + name)}")
        s.out(theme.c("dim", t("example.hint")))
        return
    name = args[0].lower()
    lines = content.example_lines(name)
    if lines is None:
        raise QFError("err.unknown_example", name=args[0])
    s.out(theme.c("bold", t("example.running", desc=t("example." + name))))
    run_script(s, lines)
    s.out(render.circuit(s.machine.circuit, s.machine.n))


@command("explain", "explain [on|off]", "learn")
def cmd_explain(s, args):
    if args and args[0].lower() in ("on", "off"):
        s.explain = args[0].lower() == "on"
    else:
        s.explain = not s.explain
    s.out(t("explain.on" if s.explain else "explain.off"))


@command("help", "help [command]", "learn")
def cmd_help(s, args):
    if args:
        name = resolve(args[0].lower())
        if name is None:
            raise QFError("err.unknown_command", cmd=args[0])
        cmd = REGISTRY[name]
        key = f"gate.{name}" if cmd.category == "gates" else f"cmd.{name}"
        s.out(f"{theme.c('cyan', cmd.usage)}\n  {t(key)}")
        return
    s.out(theme.c("bold yellow", t("help.title")))
    for cat in CATEGORIES:
        s.out("\n" + theme.c("bold", t(f"cat.{cat}")))
        if cat == "gates":
            for kind in ("single", "rotation", "controlled", "swap"):
                names = " ".join(g.name for g in GATES.values() if g.kind == kind)
                s.out(f"  {theme.c('cyan', names)}   {theme.c('dim', t('gates.' + kind))}")
            continue
        for cmd in REGISTRY.values():
            if cmd.category == cat:
                s.out(f"  {theme.c('cyan', f'{cmd.usage:<18}')} {t(f'cmd.{cmd.name}')}")
    s.out("\n" + theme.c("dim", t("help.more")))


@command("lang", "lang [code]")
def cmd_lang(s, args):
    langs = i18n.available()
    if not args:
        s.out(t("lang.current", code=i18n.current()))
        for code, name in langs.items():
            s.out(f"  {theme.c('cyan', code)}  {name}")
        return
    if not i18n.set_language(args[0]):
        raise QFError("err.unknown_lang", code=args[0], langs=", ".join(langs))
    s.out(t("lang.set", name=langs[i18n.current()]))


@command("clear")
def cmd_clear(s, args):
    s.out("\033[2J\033[H" if theme.enabled else "\n" * 3)


@command("quit")
def cmd_quit(s, args):
    s.out(t("quit.bye"))
    raise QuitShell


def execute_line(s, line):
    line = line.split("#")[0].strip()
    if not line:
        return
    word, *args = line.split()
    word = word.lower()
    name = resolve(word)
    if name is None:
        msg = t("err.unknown_command", cmd=word)
        close = difflib.get_close_matches(word, [*REGISTRY, *i18n.aliases()], n=1, cutoff=0.6)
        if close:
            msg += " " + t("err.did_you_mean", s=close[0])
        s.out(theme.err(msg + " " + t("err.try_help")))
        return
    try:
        REGISTRY[name].func(s, args)
    except QFError as e:
        s.out(theme.err(t(e.key, **e.params)))
