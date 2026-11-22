from .statevector import StateVector

POLES = {
    "|0>": (0, 0, 1), "|1>": (0, 0, -1),
    "|+>": (1, 0, 0), "|->": (-1, 0, 0),
    "|+i>": (0, 1, 0), "|-i>": (0, -1, 0),
}


def bloch(sv: StateVector, q: int) -> tuple[float, float, float, float]:
    """Coordinate (x, y, z) del qubit q sulla sfera di Bloch, più la purezza."""
    bit = 1 << q
    r00 = r11 = 0.0
    r01 = 0j
    for i in range(sv.dim):
        if i & bit:
            continue
        a0, a1 = sv.amps[i], sv.amps[i | bit]
        r00 += abs(a0) ** 2
        r11 += abs(a1) ** 2
        r01 += a0 * a1.conjugate()
    x, y, z = 2 * r01.real, -2 * r01.imag, r00 - r11
    # 1 = stato puro, 0.5 = qubit entangled al massimo
    return x, y, z, (1 + x * x + y * y + z * z) / 2


def named_state(x, y, z) -> str | None:
    for name, (a, b, c) in POLES.items():
        if abs(x - a) + abs(y - b) + abs(z - c) < 1e-6:
            return name
