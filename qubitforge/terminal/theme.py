import os
import sys

CODES = {"dim": "2", "bold": "1", "red": "31", "green": "32", "yellow": "33",
         "blue": "34", "magenta": "35", "cyan": "36"}
enabled = False


def setup(no_color=False):
    global enabled
    enabled = sys.stdout.isatty() and not no_color and "NO_COLOR" not in os.environ


def c(style, text, readline=False):
    """Colora il testo. Con readline=True protegge i codici per l'uso nel prompt."""
    if not enabled:
        return text
    start = "\033[" + ";".join(CODES[s] for s in style.split()) + "m"
    end = "\033[0m"
    if readline:
        start, end = f"\001{start}\002", f"\001{end}\002"
    return start + text + end


def err(text):
    return c("red", text)
