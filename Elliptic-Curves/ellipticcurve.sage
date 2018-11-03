from sage.all import *

def _EllipticCurve(p, a, b):
    E = EllipticCurve(GF(p), [a, b])
    return E

def _add(P, Q):
    return P + Q

def _scalar_mul(c, P):
    return c*P

def _testECC():
    """
    Reference: https://ctftime.org/task/6860

    Testing validity for single instance
    """
    # Defining the Elliptic Curve
    p = 889774351128949770355298446172353873
    a = 12345
    b = 67890
    E = _EllipticCurve(p, a, b)

    # Defining points on the Elliptic Curve
    px, py = (238266381988261346751878607720968495, 591153005086204165523829267245014771)
    qx, qy = (341454032985370081366658659122300896, 775807209463167910095539163959068826)
    P = E((px, py))
    Q = E((qx, qy))

    P_plus_Q = E((323141381196798033512190262227161667, 775010084514487531788273912037060561))
    twelveP = E((771157329084582589666569152178346504, 869049850567812139357308211622374273))

    try:
        assert _add(P, Q) == P_plus_Q
        assert _scalar_mul(12, P) == twelveP
    except:
        return -1
    return 1

if _testECC() == 1:
    print "[+] Test Passed!"
else:
    print "[-] Test Failed!"
