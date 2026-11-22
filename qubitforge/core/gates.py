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
        arguments = ["<angle>"] * self.params
        if self.controls == 1:
            arguments.append("<c>")
        elif self.controls > 1:
            for number in range(1, self.controls + 1):
                arguments.append(f"<c{number}>")

        if self.targets == 2:
            arguments.extend(["<a>", "<b>"])
        elif self.controls:
            arguments.append("<t>")
        else:
            arguments.append("<q>")
        return " ".join([self.name, *arguments])

    @property
    def kind(self):
        if self.base == "swap":
            return "swap"
        if self.controls:
            return "controlled"
        return "rotation" if self.params else "single"


GATES = {name: GateSpec(name, name) for name in FIXED}

for name in ("rx", "ry", "rz", "p"):
    GATES[name] = GateSpec(name, name, params=1)

for base in ("x", "y", "z", "h"):
    name = "c" + base
    GATES[name] = GateSpec(name, base, controls=1)

GATES["cp"] = GateSpec("cp", "p", controls=1, params=1)
GATES["ccx"] = GateSpec("ccx", "x", controls=2)
GATES["swap"] = GateSpec("swap", "swap", targets=2)


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
