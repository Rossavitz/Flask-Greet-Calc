from flask import Flask, request

app = Flask(__name__)

"""Basic math operations."""


def add(a, b):
    """Add a and b."""

    return a + b


def sub(a, b):
    """Substract b from a."""
    return a - b


def mult(a, b):
    """Multiply a and b."""
    return a * b


def div(a, b):
    """Divide a by b."""
    return a / b


@app.route("/add")
def addition():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = add(a, b)
    return str(total)


@app.route("/sub")
def subtraction():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = sub(a, b)
    return str(total)


@app.route("/mult")
def multiply():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = mult(a, b)
    return str(total)


@app.route("/div")
def divide():
    """Add a and b parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = div(a, b)
    return str(total)


math_funcs = {"add": add, "sub": sub, "mult": mult, "div": div}


@app.route("/math/<operation>")
def do_math(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    total = math_funcs[operation](a, b)
    return str(total)
