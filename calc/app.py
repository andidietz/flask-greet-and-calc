from flask import Flask, request
from operations import *
app = Flask(__name__)

@app.route('/add')
def add(a,b):
    """Adds intergers a and b"""

    args = assign_args(request)
    # Source: Needing to return a str in this function config (6/30/2021): Exercise Solution
    return str(add(args['a'], args['b']))

@app.route('/sub')
def sub():
    """Subtracts intergers a and b"""

    args = assign_args(request)
    return str(sub(args['a'], args['b']))

@app.route('/mult')
def mult():
    """Multiples intergers a and b"""

    args = assign_args(request)
    return str(mult(args['a'], args['b']))

@app.route('/div')
def div():
    """Divides intergers a and b"""

    args = assign_args(request)
    return str(div(args['a'], args['b']))