import cmath
import math
from dataclasses import dataclass

Matrix = tuple[complex, complex, complex, complex]
SQ2 = 1 / math.sqrt(2)

FIXED: dict[str, Matrix] = {
    "id": (1, 0, 0, 1),
    "x": (0, 1, 1, 0),
    "y": (0, -1j, 1j, 0),
    "z": (1, 0, 0, -1),
    "h": (SQ2, SQ2, SQ2, -SQ2),
    "s": (1, 0, 0, 1j),
    "sdg": (1, 0, 0, -1j),
    "t": (1, 0, 0, cmath.exp(1j * math.pi / 4)),
    "tdg": (1, 0, 0, cmath.exp(-1j * math.pi / 4)),
}


@dataclass(frozen=True)
class GateSpec:
    name: str
    base: str                  # porta su cui agisce: x, z, rx, p, swap...
    controls: int = 0
    params: int = 0
    targets: int = 1

    @property
    def arity(self):
        return self.controls + self.targets

    @property
    def usage(self):
        if self.controls == 1:
            ctrl = " <c>"
        else:
            ctrl = "".join(f" <c{i}>" for i in range(1, self.controls + 1))
        if self.targets == 2:
            tgt = " <a> <b>"
        else:
            tgt = " <t>" if self.controls else " <q>"
        return self.name + " <angle>" * self.params + ctrl + tgt

    @property
    def kind(self):
        if self.base == "swap":
            return "swap"
        if self.controls:
            return "controlled"
        return "rotation" if self.params else "single"


GATES = {g.name: g for g in [
    *(GateSpec(n, n) for n in ("id", "x", "y", "z", "h", "s", "sdg", "t", "tdg")),
    *(GateSpec(n, n, params=1) for n in ("rx", "ry", "rz", "p")),
    GateSpec("cx", "x", controls=1),
    GateSpec("cy", "y", controls=1),
    GateSpec("cz", "z", controls=1),
    GateSpec("ch", "h", controls=1),
    GateSpec("cp", "p", controls=1, params=1),
    GateSpec("ccx", "x", controls=2),
    GateSpec("swap", "swap", targets=2),
]}


def matrix(base, params=()) -> Matrix:
    if base in FIXED:
        return FIXED[base]
    theta = params[0]
    if base == "p":
        return (1, 0, 0, cmath.exp(1j * theta))
    c, s = math.cos(theta / 2), math.sin(theta / 2)
    if base == "rx":
        return (c, -1j * s, -1j * s, c)
    if base == "ry":
        return (c, -s, s, c)
    if base == "rz":
        return (cmath.exp(-1j * theta / 2), 0, 0, cmath.exp(1j * theta / 2))
    raise KeyError(base)
