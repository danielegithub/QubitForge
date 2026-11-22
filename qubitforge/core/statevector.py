"""Il qubit 0 è il bit meno significativo: |q2 q1 q0> ha indice q2*4 + q1*2 + q0."""
import math

from .gates import Matrix


class StateVector:
    def __init__(self, n):
        self.n = n
        self.dim = 1 << n
        self.amps = [0j] * self.dim
        self.amps[0] = 1 + 0j

    def apply(self, m: Matrix, target, controls=()):
        bit = 1 << target
        cmask = sum(1 << c for c in controls)
        m00, m01, m10, m11 = m
        for i in range(self.dim):
            if i & bit or i & cmask != cmask:
                continue
            j = i | bit
            a, b = self.amps[i], self.amps[j]
            self.amps[i] = m00 * a + m01 * b
            self.amps[j] = m10 * a + m11 * b

    def prob_one(self, q):
        return sum(abs(a) ** 2 for i, a in enumerate(self.amps) if i >> q & 1)

    def collapse(self, q, outcome, p_one):
        norm = math.sqrt(p_one if outcome else 1 - p_one)
        for i in range(self.dim):
            if i >> q & 1 == outcome:
                self.amps[i] /= norm
            else:
                self.amps[i] = 0j

    def probabilities(self):
        return [abs(a) ** 2 for a in self.amps]

    def label(self, index):
        return format(index, f"0{self.n}b")
