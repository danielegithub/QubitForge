from ..lang import commands
from ..lang.session import QuitShell, Session
from . import theme


def prompt(s: Session):
    return (theme.c("bold magenta", f"qf[{s.machine.n}q]", readline=True)
            + theme.c("bold", "> ", readline=True))


def run(s: Session):
    try:
        import readline  # noqa: F401 (frecce e cronologia nell'input)
    except ImportError:
        pass
    while True:
        try:
            line = input(prompt(s))
        except EOFError:
            print()
            return
        except KeyboardInterrupt:
            print()
            continue
        try:
            commands.execute_line(s, line)
        except QuitShell:
            return
