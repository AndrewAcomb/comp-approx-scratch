from math import pi
from fractions import Fraction

def series(r_a, r_b):
    return r_a + r_b

def parallel(r_a, r_b):
    return (r_a * r_b) / (r_a + r_b)

def approximate_resistor_l1(n, r_t, r_0):
    ops = []
    a, b = 0, 1
    c, d = 1, 0
    target = r_t/r_0
    for _ in range(n):
        M = Fraction(a+c, b+d)
        if M < target:
            a, b = M.numerator, M.denominator
            ops.append("+")
        elif M > target:
            c, d = M.numerator, M.denominator
            ops.append("//")
        else:
            break
            
    print(M.numerator/M.denominator * r_0)

    last = "(" * len(ops) + str(r_0)
    while ops:
        last += ops.pop() + str(r_0) + ")"

    return last


ex1 = approximate_resistor_l1(8, pi, 4)
print(ex1)





