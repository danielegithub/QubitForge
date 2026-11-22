"""Traduzioni: un JSON per lingua in locales/. Le chiavi che mancano ricadono sull'inglese.

Per aggiungere una lingua basta copiare en.json e tradurlo (le lezioni
sono facoltative, vanno in learn/lessons/<codice>/).
"""
import json
import os
from pathlib import Path

LOCALES = Path(__file__).parent / "locales"
DEFAULT = "en"

_cache = {}
_current = DEFAULT


def _load(code):
    if code not in _cache:
        path = LOCALES / f"{code}.json"
        _cache[code] = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    return _cache[code]


def available():
    """{codice: nome nativo} per ogni lingua installata."""
    return {p.stem: _load(p.stem).get("meta.name", p.stem) for p in sorted(LOCALES.glob("*.json"))}


def current():
    return _current


def set_language(code):
    global _current
    code = code.lower().split("_")[0].split("-")[0]
    if code not in available():
        return False
    _current = code
    return True


def detect():
    for var in ("QUBITFORGE_LANG", "LC_ALL", "LC_MESSAGES", "LANG"):
        code = os.environ.get(var, "").lower().split(".")[0].split("_")[0]
        if code in available():
            return code
    return DEFAULT


def t(key, **kw):
    val = _load(_current).get(key)
    if val is None:
        val = _load(DEFAULT).get(key, key)
    if isinstance(val, str) and kw:
        try:
            return val.format(**kw)
        except (KeyError, IndexError):
            pass
    return val


def aliases():
    """Alias dei comandi di tutte le lingue; quelli della lingua corrente vincono."""
    merged = {}
    for code in [*available(), _current]:
        merged.update(_load(code).get("aliases", {}))
    return merged
