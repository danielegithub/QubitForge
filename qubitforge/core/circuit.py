from dataclasses import dataclass


@dataclass(frozen=True)
class Instruction:
    name: str                  # h, cx, rx... oppure "measure"
    qubits: tuple[int, ...]
    params: tuple[float, ...] = ()


class Circuit:
    def __init__(self):
        self.instructions: list[Instruction] = []

    def __len__(self):
        return len(self.instructions)

    def append(self, ins):
        self.instructions.append(ins)

    def truncate(self, k):
        del self.instructions[k:]

    def to_script(self, n):
        lines = [f"qreg {n}"]
        for ins in self.instructions:
            args = [*map(repr, ins.params), *map(str, ins.qubits)]
            lines.append(" ".join([ins.name, *args]))
        return "\n".join(lines) + "\n"

    def to_qasm(self, n):
        out = ["OPENQASM 2.0;", 'include "qelib1.inc";', f"qreg q[{n}];", f"creg c[{n}];"]
        for ins in self.instructions:
            qs = ",".join(f"q[{q}]" for q in ins.qubits)
            if ins.name == "measure":
                q = ins.qubits[0]
                out.append(f"measure q[{q}] -> c[{q}];")
            elif ins.params:
                out.append(f"{ins.name}({ins.params[0]!r}) {qs};")
            else:
                out.append(f"{ins.name} {qs};")
        return "\n".join(out) + "\n"
