"""Calcolo degli angoli scritti a mano: pi/2, 3*pi/4, -0.5, sqrt(2)."""
import ast
import math
import operator

from ..core.errors import QFError

OPS = {ast.Add: operator.add, ast.Sub: operator.sub,
       ast.Mult: operator.mul, ast.Div: operator.truediv}
NAMES = {"pi": math.pi, "tau": 2 * math.pi}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.Constant) and type(node.value) in (int, float):
        return float(node.value)
    if isinstance(node, ast.Name) and node.id in NAMES:
        return NAMES[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.USub, ast.UAdd)):
        v = _eval(node.operand)
        return -v if isinstance(node.op, ast.USub) else v
    if isinstance(node, ast.BinOp) and type(node.op) in OPS:
        return OPS[type(node.op)](_eval(node.left), _eval(node.right))
    if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
            and node.func.id == "sqrt" and len(node.args) == 1 and not node.keywords):
        return math.sqrt(_eval(node.args[0]))
    raise ValueError


def eval_angle(text):
    try:
        return _eval(ast.parse(text.replace("π", "pi"), mode="eval"))
    except (ValueError, SyntaxError, ZeroDivisionError, OverflowError):
        raise QFError("err.bad_angle", text=text) from None
