import random
from collections import Counter

from .circuit import Circuit, Instruction
from .errors import QFError
from .gates import GATES, matrix
from .statevector import StateVector

MAX_QUBITS = 14


class Machine:
    def __init__(self, n=2, seed=None):
        self.rng = random.Random(seed)
        self.reset(n)

    def reset(self, n=None):
        if n is None:
            n = self.n
        if not 1 <= n <= MAX_QUBITS:
            raise QFError("err.qreg_range", max=MAX_QUBITS)
        self.n = n
        self.sv = StateVector(n)
        self.circuit = Circuit()
        self.history = []

    def check_qubits(self, qubits):
        for q in qubits:
            if not 0 <= q < self.n:
                raise QFError("err.qubit_range", q=q, last=self.n - 1)
        if len(set(qubits)) != len(qubits):
            raise QFError("err.qubit_dup")

    def execute(self, ins: Instruction):
        """Esegue l'istruzione; per `measure` restituisce il bit letto."""
        if ins.name == "measure":
            self.check_qubits(ins.qubits)
            return self.measure(ins)
        spec = GATES.get(ins.name)
        if spec is None:
            raise QFError("err.unknown_gate", name=ins.name)
        if len(ins.qubits) != spec.arity or len(ins.params) != spec.params:
            raise QFError("err.arity", usage=spec.usage)
        self.check_qubits(ins.qubits)
        self.save_state()
        if spec.base == "swap":
            a, b = ins.qubits
            x = matrix("x")
            self.sv.apply(x, b, (a,))
            self.sv.apply(x, a, (b,))
            self.sv.apply(x, b, (a,))
        else:
            controls = ins.qubits[:spec.controls]
            self.sv.apply(matrix(spec.base, ins.params), ins.qubits[-1], controls)
        self.circuit.append(ins)

    def measure(self, ins):
        q = ins.qubits[0]
        self.save_state()
        p1 = self.sv.prob_one(q)
        outcome = int(self.rng.random() < p1)
        self.sv.collapse(q, outcome, p1)
        self.circuit.append(ins)
        return outcome

    def sample(self, shots):
        """Ripete l'esperimento senza toccare lo stato."""
        picks = self.rng.choices(range(self.sv.dim), weights=self.sv.probabilities(), k=shots)
        counts = Counter(self.sv.label(i) for i in picks)
        return dict(sorted(counts.items()))

    def save_state(self):
        self.history.append((self.sv.amps[:], len(self.circuit)))

    def undo(self):
        if not self.history:
            return False
        self.sv.amps, k = self.history.pop()
        self.circuit.truncate(k)
        return True
