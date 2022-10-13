from fractions import Fraction

x = 0
y = 0
z = 0
w = 0

def init(a, b, c, d):
    global x
    global y
    global z
    global w
    x = a
    y = b
    z = c
    w = d

def sub_frac(a, b, c, d):
    frac1 = Fraction(a, b)
    print(frac1)
    frac2 = Fraction(c, d)
    print(frac2)
    return frac1 - frac2

def sub_comp(a, b, c, d):
    comp1 = complex(a, b)
    print(comp1)
    comp2 = complex(c, d)
    print(comp2)
    return comp1 - comp2