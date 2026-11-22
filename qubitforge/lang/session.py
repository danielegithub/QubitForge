from dataclasses import dataclass, field
from typing import Callable

from ..core.machine import Machine


class QuitShell(Exception):
    pass


@dataclass
class Session:
    machine: Machine = field(default_factory=Machine)
    explain: bool = False
    out: Callable[[str], None] = print
    depth: int = 0          # quanti load/example sono annidati
