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
        target_bit = 1 << target
        control_bits = sum(1 << qubit for qubit in controls)
        m00, m01, m10, m11 = m

        # La porta agisce sulle coppie che differiscono solo nel bit bersaglio.
        for zero_index in range(self.dim):
            if zero_index & target_bit:
                continue
            if (zero_index & control_bits) != control_bits:
                continue
            one_index = zero_index | target_bit
            amp_zero = self.amps[zero_index]
            amp_one = self.amps[one_index]
            self.amps[zero_index] = m00 * amp_zero + m01 * amp_one
            self.amps[one_index] = m10 * amp_zero + m11 * amp_one

    def prob_one(self, q):
        bit = 1 << q
        return sum(abs(amplitude) ** 2 for index, amplitude in enumerate(self.amps) if index & bit)

    def collapse(self, q, outcome, p_one):
        probability = p_one if outcome else 1 - p_one
        norm = math.sqrt(probability)
        for index in range(self.dim):
            measured_bit = (index >> q) & 1
            if measured_bit == outcome:
                self.amps[index] /= norm
            else:
                self.amps[index] = 0j

    def probabilities(self):
        return [abs(a) ** 2 for a in self.amps]

    def label(self, index):
        return format(index, f"0{self.n}b")
