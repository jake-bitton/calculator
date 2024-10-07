"""
Store logic for processing all supported calculator actions
"""

def add(a: int | float, b: int | float) -> int | float:
    return a+b

def subtract(a: int | float, b: int | float) -> int | float:
    return a-b

def multiply(a: int | float, b: int | float) -> int | float:
    return a*b

def divide(a: int | float, b: int | float) -> int | float:
    return a/b

def exponent(a: int|float, power: int) -> int | float:
    #  Need to add functionality to exponentiate by fractional/decimal values
    exp = a
    for i in range(power-1):
        exp *= exp*a
    return exp

def n_root(a: int|float, n: int|float) -> int|float:
    #  To be implemented
    pass

def sin_rad(theta: int|float) -> int | float:
    # T B I
    pass

def cos_rad(theta: int|float) -> int | float:
    # T B I
    pass

def tan_rad(theta: int|float) -> int | float:
    # T B I
    pass