"""
 Author: Aidan Kiser
 Version: 13 September 2024
"""

def performAdd(p, q):
    return p + q 

def performSub(a, b):
    return a - b 

def performMutiply(c, d):
    return c * d

def performDivide(e, f):
    try:
        return e / f
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."