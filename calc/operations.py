
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

def assign_args(request):
    """Assigns args to variables"""
    
    a = int(request.args['a'])
    b = int(request.args['b'])
    
    return {'a': a, 'b': b}