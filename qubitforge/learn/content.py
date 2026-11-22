from pathlib import Path

BASE = Path(__file__).parent
EXAMPLES = BASE / "examples"
LESSONS = BASE / "lessons"
FALLBACK = "en"


def example_names():
    return sorted(p.stem for p in EXAMPLES.glob("*.qf"))


def example_lines(name):
    path = EXAMPLES / f"{name}.qf"
    if path.is_file():
        return path.read_text(encoding="utf-8").splitlines()


def _lesson_files(lang):
    folder = LESSONS / lang
    if not any(folder.glob("*.md")):
        folder = LESSONS / FALLBACK
    return sorted(folder.glob("*.md"))


def _read(path):
    """Titolo (prima riga, senza #) e corpo della lezione."""
    first, *rest = path.read_text(encoding="utf-8").splitlines()
    return first.lstrip("# ").strip(), "\n".join(rest).strip("\n")


def lessons(lang):
    return [(int(p.name.split("-")[0]), _read(p)[0]) for p in _lesson_files(lang)]


def lesson(lang, number):
    for p in _lesson_files(lang):
        if int(p.name.split("-")[0]) == number:
            return _read(p)
