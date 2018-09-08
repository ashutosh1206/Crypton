from sage.all import *

def wiener(e, n):
    m = 12345
    c = pow(m, e, n)
    lst = continued_fraction(Integer(e)/Integer(n))
    conv = lst.convergents()
    for i in conv:
        k = i.numerator()
        d = int(i.denominator())
        try:
            m1 = pow(c, d, n)
            if m1 == m:
                print "[*] Found d: ", d
                return d
        except:
            continue
    return -1
