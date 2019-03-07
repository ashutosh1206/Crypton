from sage.all import *
import random

def brute_ecdlp(P, Q, E):
    """
    Brute Force algorithm to solve ECDLP and retrieve value of secret key `x`.
    Use only if group is very small.
    Includes memoization for faster computation
    [Warning]: Tested for Weierstrass Curves only

    :parameters:
        E : sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field_with_category
            Elliptic Curve defined as y^2 = x^3 + a*x + b mod p
        P : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            Base point of the Elliptic Curve E
        Q : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            Q = x*P, where `x` is the secret key
    """
    _order = P.order()
    try:
        assert P == E((P[0], P[1]))
    except TypeError:
        print "[-] Point does not lie on the curve"
        return -1

    res = 2*P
    if res == Q:
        return 2
    if Q == E((0, 1, 0)):
        return _order
    if Q == P:
        return 1
    i = 3
    while i <= P.order() - 1:
        res = res + P
        if res == Q:
            return i
        i += 1
    return -1


if __name__ == "__main__":
    E = EllipticCurve(GF(17), [2, 2])
    P = E((5, 1))
    try:
        for _ in range(100):
            x = random.randint(2, 18)
            assert brute_ecdlp(E((5, 1)), x*P, E) == x
    except Exception as e:
        print e
        print "[-] Function inconsistent and incorrect"
        print "[-] Check your implementation"
