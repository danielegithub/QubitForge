import sys
import time

from .. import i18n
from . import theme

TITLE = "Q U B I T F O R G E"


def banner():
    inner = f"  ⟨0|  {TITLE}  |1⟩  "
    box = ["╭" + "─" * len(inner) + "╮", "│" + inner + "│", "╰" + "─" * len(inner) + "╯"]
    return theme.c("bold cyan", "\n".join(box))


def run(fast=False):
    animate = sys.stdout.isatty() and not fast
    for line in i18n.t("boot.lines"):
        print(f"  {theme.c('green', '[ OK ]')} {line}", flush=True)
        if animate:
            time.sleep(0.12)
    print()
    print(banner())
    print(theme.c("dim", "  " + i18n.t("boot.version")))
    print()
    print(i18n.t("boot.ready"))
    print(theme.c("dim", i18n.t("boot.hint")))
    print()
