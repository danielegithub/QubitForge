import argparse

from . import i18n
from .core.machine import Machine
from .lang import commands
from .lang.session import QuitShell, Session
from .terminal import boot, shell, theme


def main(argv=None):
    parser = argparse.ArgumentParser(prog="qubitforge", description="Quantum computer simulator for learning.")
    parser.add_argument("script", nargs="?", help="optional .qf file to run before the prompt")
    parser.add_argument("--lang", help="interface language (default: auto-detect)")
    parser.add_argument("--seed", type=int, help="random seed (reproducible measurements)")
    parser.add_argument("--fast", action="store_true", help="skip the boot animation")
    parser.add_argument("--no-color", action="store_true", help="disable colors")
    args = parser.parse_args(argv)

    theme.setup(args.no_color)
    if not (args.lang and i18n.set_language(args.lang)):
        i18n.set_language(i18n.detect())

    session = Session(Machine(2, seed=args.seed))
    boot.run(fast=args.fast)
    try:
        if args.script:
            commands.execute_line(session, f"load {args.script}")
        shell.run(session)
    except QuitShell:
        pass


if __name__ == "__main__":
    main()
