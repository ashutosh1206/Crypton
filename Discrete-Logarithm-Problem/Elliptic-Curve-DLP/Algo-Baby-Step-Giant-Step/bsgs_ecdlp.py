from sage.all import *

def bsgs_ecdlp(P, Q, E):
    if Q == E((0, 1, 0)):
        return P.order()
    if Q == P:
        return 1
    m = ceil(sqrt(P.order()))
    lookup_table = {j*P: j for j in range(m)}
    for i in range(m):
        temp = Q - (i*m)*P
        if temp in lookup_table:
            return (i*m + lookup_table[temp]) % P.order()
    return None

if __name__ == "__main__":
    import random
    E = EllipticCurve(GF(17), [2, 2])
    try:
        for i in range(100):
            x = random.randint(2, 19)
            assert bsgs_ecdlp(E((5, 1)), x*E((5, 1)), E) == x
    except Exception as e:
        print e
        print "[-] Something's wrong!"
