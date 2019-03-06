from Crypto.Util.number import *

def brute_dlp(g, y, p):
    mod_size = len(bin(p-1)[2:])
    sol = pow(g, 2, p)
    if y == 1:
        return 0
    if y == g:
        return 1
    if sol == y:
        return y
    i = 3
    while i <= p-1:
        sol = sol*g % p
        if sol == y:
            return i
        i += 1
    return None

def pohlig_hellman_pp(g, y, p, q, e):
    """
    Reference: http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf

    Computes `x` = a mod (p-1) for the DLP g**x % p == y
    in the Group G = {0, 1, 2, ..., p-1}
    given that order `n` = p-1 is a power of a small prime,
    ie. n = p-1 = q**e, where q is a small prime

    :parameters:
        g : int/long
                Generator of the group
        y : int/long
                Result of g**x % p
        p : int/long
                Group over which DLP is generated. Commonly p is a prime number
        e : int/long
                Exponent of 2 in the group order: n = p-1 = q**e
    """

    try:
        assert p-1 == q**e
        # Assume q is a factor of p-1
        assert (p-1) % q == 0
    except:
        print "[-] Error! q**e not a factor of p-1"
        return -1

    # a = a_0*(q**0) + a_1*(q**1) + a_2*(q**2) + ... + a_(e-1)*(q**(e-1)) + s*(q**e)
    # where a_0, a_1, a_2, ..., a_(e-1) belong to {0,1,...,q-1} and s is some integer
    a = 0

    b_j = y
    alpha = pow(g, (p-1)/q, p)
    for j in range(e):
        y_i = pow(b_j, (p-1)/(q**(j+1)), p)
        a_j = brute_dlp(alpha, y_i, p)
        assert a_j >= 0 and a_j <= q-1
        a += a_j*(q**j)

        multiplier = pow(g, a_j*(q**j), p)
        assert GCD(multiplier, p) == 1
        b_j = (b_j * inverse(multiplier, p)) % p
    return a

if __name__ == "__main__":
    assert pow(3, pohlig_hellman_pp(3, 188, 257, 2, 8), 257) == 188
