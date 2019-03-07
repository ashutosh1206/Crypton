from sage.all import *
from Crypto.Util.number import *

def func_f(X_i, P, Q, E):
    """
        To calculate X_(i+1) = f(X_i)

        :parameters:
            X_i : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
                X_i = (a_i * P) + (b_i * Q)
            P : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
                Base point on which ECDLP is defined
            Q : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
                Q = x*P, where `x` is the secret key
            E : sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field_with_category
                Elliptic Curve defined as y^2 = x^3 + a*x + b mod p
    """
    try:
        # Point P and Q should lie on the Elliptic Curve E
        assert P == E((P[0], P[1]))
        assert Q == E((Q[0], Q[1]))
    except Exception as e:
        # Do not return anything if the point is invalid
        print "[-] Point does not lie on the curve!"
        return None
    if int(X_i[0]) % 3 == 2:
        # Partition S_1
        return X_i + Q
    if int(X_i[0]) % 3 == 0:
        # Partition S_2
        return 2*X_i
    if int(X_i[0]) % 3 == 1:
        # Partition S_3
        return X_i + P
    else:
        print "[-] Something's Wrong!"
        return -1

def func_g(a, P, X_i, E):
    """
    Calculate a_(i+1) = g(a)

    :parameters:
        a : int/long
            Equivalent to a_i in X_i = a_i*P + b_i*Q
        P : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            Base point on which ECDLP is defined
        X_i : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            X_i = a_i*P + b_i*Q
        E : sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field_with_category
            Elliptic Curve defined as y^2 = x^3 + a*x + b mod p
    """
    try:
        assert P == E((P[0], P[1]))
    except Exception as e:
        print e
        print "[-] Point does not lie on the curve"
        return None
    n = P.order()
    if int(X_i[0]) % 3 == 2:
        # Partition S_1
        return a
    if int(X_i[0]) % 3 == 0:
        # Partition S_2
        return 2*a % n
    if int(X_i[0]) % 3 == 1:
        # Partition S_3
        return (a + 1) % n
    else:
        print "[-] Something's Wrong!"
        return None

def func_h(b, P, X_i, E):
    """
    Calculate a_(i+1) = g(a)

    :parameters:
        a : int/long
            Equivalent to a_i in X_i = a_i*P + b_i*Q
        P : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            Base point on which ECDLP is defined
        X_i : sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_finite_field
            X_i = a_i*P + b_i*Q
        E : sage.schemes.elliptic_curves.ell_finite_field.EllipticCurve_finite_field_with_category
            Elliptic Curve defined as y^2 = x^3 + a*x + b mod p
    """
    try:
        assert P == E((P[0], P[1]))
    except Exception as e:
        print e
        print "[-] Point does not lie on the curve"
        return None
    n = P.order()
    if int(X_i[0]) % 3 == 2:
        # Partition S_1
        return (b + 1) % n
    if int(X_i[0]) % 3 == 0:
        # Partition S_2
        return 2*b % n
    if int(X_i[0]) % 3 == 1:
        # Partition S_3
        return b
    else:
        print "[-] Something's Wrong!"
        return None

def pollardrho(P, Q, E):
    try:
        assert P == E((P[0], P[1]))
        assert Q == E((Q[0], Q[1]))
    except Exception as e:
        print e
        print "[-] Point does not lie on the curve"
        return None
    n = P.order()

    for j in range(10):
        a_i = random.randint(2, P.order()-2)
        b_i = random.randint(2, P.order()-2)
        a_2i = random.randint(2, P.order()-2)
        b_2i = random.randint(2, P.order()-2)

        X_i = a_i*P + b_i*Q
        X_2i = a_2i*P + b_2i*Q

        i = 1
        while i <= n:
            # Single Step Calculations
            a_i = func_g(a_i, P, X_i, E)
            b_i = func_h(b_i, P, X_i, E)
            X_i = func_f(X_i, P, Q, E)

            # Double Step Calculations
            a_2i = func_g(func_g(a_2i, P, X_2i, E), P, func_f(X_2i, P, Q, E), E)
            b_2i = func_h(func_h(b_2i, P, X_2i, E), P, func_f(X_2i, P, Q, E), E)
            X_2i = func_f(func_f(X_2i, P, Q, E), P, Q, E)

            if X_i == X_2i:
                if b_i == b_2i:
                    break
                assert GCD(b_2i - b_i, n) == 1
                return ((a_i - a_2i) * inverse(b_2i - b_i, n)) % n
            else:
                i += 1
                continue

if __name__ == "__main__":
    import random
    for i in range(100):
        E = EllipticCurve(GF(17), [2, 2])
        P = E((5, 1))
        x = random.randint(2, P.order()-2)
        Q = x*P
        assert pollardrho(P, Q, E)*P == Q
