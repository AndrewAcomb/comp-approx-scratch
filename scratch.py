from math import pi
from fractions import Fraction

def series(r_a, r_b):
    return r_a + r_b

def parallel(r_a, r_b):
    return (r_a * r_b) / (r_a + r_b)


def get_operations(n, target):
    result = []

    a, b = 0, 1
    c, d = 1, 0
    for _ in range(n):
        M = Fraction(a+c, b+d)
        print(M, M.numerator/M.denominator, target)
        if M < target:
            a, b = M.numerator, M.denominator
            result.append("+")
        elif M > target:
            c, d = M.numerator, M.denominator
            result.append("//")
        else:
            return result
        
    return result


def stringify_ops(ops, resistor_str):
    last = resistor_str
    while ops:
        last = "(" + last + ops.pop() + resistor_str + ")"
    return last


def approximate_resistor_l1(n, r_t, r_0):
    ops = get_operations(n, r_t/r_0)
    return stringify_ops(ops, str(r_0))


print(approximate_resistor_l1(5, pi, 2))





