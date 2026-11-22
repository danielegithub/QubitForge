import math
from fractions import Fraction

from .. import i18n
from ..core.analysis import bloch, named_state
from ..core.circuit import Circuit
from ..core.gates import GATES
from ..core.machine import Machine
from . import theme

BAR = 28
MAX_ROWS = 32


def bar(p):
    return "█" * round(p * BAR)


def fmt_angle(x):
    f = Fraction(x / math.pi).limit_denominator(12)
    if abs(float(f) * math.pi - x) > 1e-9:
        return f"{x:.3g}"
    if f == 0:
        return "0"
    num, den = f.numerator, f.denominator
    s = "π" if abs(num) == 1 else f"{abs(num)}π"
    if den != 1:
        s += f"/{den}"
    return f"-{s}" if num < 0 else s


def state(m: Machine, *, show_amplitudes=True):
    vector = m.sv
    if show_amplitudes:
        header = i18n.t("state.header", n=vector.n, last=vector.n - 1)
    else:
        header = i18n.t("probs.header")
    lines = [theme.c("dim", header)]

    outcomes = []
    for index, probability in enumerate(vector.probabilities()):
        if probability > 1e-12:
            outcomes.append((index, probability))

    for index, probability in outcomes[:MAX_ROWS]:
        label = theme.c("cyan", f"|{vector.label(index)}>")
        histogram = theme.c("green", bar(probability))
        row = f"{label}  {probability * 100:6.2f}%  {histogram}"
        if show_amplitudes:
            amplitude = vector.amps[index]
            row = f"{amplitude.real:+.4f}{amplitude.imag:+.4f}i  {row}"
        lines.append("  " + row)

    hidden = len(outcomes) - MAX_ROWS
    if hidden > 0:
        lines.append(theme.c("dim", i18n.t("state.hidden", n=hidden)))
    return "\n".join(lines)


def probs(m: Machine):
    return state(m, show_amplitudes=False)


def counts(res, shots):
    lines = [theme.c("dim", i18n.t("run.header", shots=shots))]
    for label, k in res.items():
        p = k / shots
        lines.append(f"  {theme.c('cyan', f'|{label}>')}  {k:>7}  {p * 100:6.2f}%  "
                     f"{theme.c('green', bar(p))}")
    return "\n".join(lines)


def bloch_report(m: Machine, q):
    x, y, z, purity = (v + 0.0 for v in bloch(m.sv, q))   # + 0.0 evita "-0.00"
    head = i18n.t("bloch.vector", q=q, x=x, y=y, z=z, p=purity)
    name = named_state(x, y, z)
    if name:
        head += f"  = {theme.c('cyan', name)}"
    note = i18n.t("bloch.pure") if purity > 0.999 else i18n.t("bloch.entangled")
    return f"{head}\n    {theme.c('dim', note)}"


def _column(ins):
    """Cosa disegnare per un'istruzione: {qubit: simbolo}."""
    spec = GATES.get(ins.name)
    if spec is None:
        return {ins.qubits[0]: "M"}
    cells = {q: "●" for q in ins.qubits[:spec.controls]}
    targets = ins.qubits[spec.controls:]
    if spec.base == "swap":
        cells.update({q: "✕" for q in targets})
    else:
        label = spec.base.upper()
        if ins.params:
            label += f"({fmt_angle(ins.params[0])})"
        cells[targets[0]] = label
    return cells


def circuit(circ: Circuit, n):
    if not circ.instructions:
        return theme.c("dim", i18n.t("circuit.empty"))
    cols = []
    for ins in circ.instructions:
        cells = _column(ins)
        w = max(len(v) for v in cells.values()) + 2
        w += 1 - w % 2          # larghezza dispari, così il filo verticale cade al centro
        cols.append((cells, min(cells), max(cells), w))

    width = len(f"q{n - 1}")
    lines = []
    for q in range(n):
        wire = f"{f'q{q}':<{width}} ─"
        gap = " " * (width + 2)
        for cells, lo, hi, w in cols:
            if q in cells:
                label = cells[q]
                left = (w - len(label)) // 2
                wire += "─" * left + label + "─" * (w - len(label) - left)
            else:
                wire += "─" * (w // 2) + ("┼" if lo < q < hi else "─") + "─" * (w // 2)
            gap += " " * (w // 2) + ("│" if lo <= q < hi else " ") + " " * (w // 2)
        lines.append(wire + "─")
        if q < n - 1:
            lines.append(gap)
    return "\n".join(lines)
