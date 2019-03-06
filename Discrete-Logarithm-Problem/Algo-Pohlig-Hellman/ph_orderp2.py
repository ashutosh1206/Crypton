from Crypto.Util.number import *

def pohlig_hellman_p2(g, y, p, e):
    """
    Computes `x` for the DLP y = g**x % p in the Group G = {0, 1, 2, ..., p-1},
    given that order of the group `n` is a power of 2, ie. n = p-1 = 2**e.

    Note that to solve the DLP using this code, `g` must be the generator.

    :parameters:
        g : int/long
                Generator of the group
        y : int/long
                Result of g**x % p
        p : int/long
                Group over which DLP is generated. Commonly p is a prime number
        e : int/long
                Exponent of 2 in the group order: n = p-1 = 2**e
    """
    try:
        assert 2**e == p - 1
    except:
        print "[-] Error! 2**e is not equal to order!"
        return -1

    k = e
    # x is a `k` bit number, max value of x is (2**k - 1)
    # x = (c_0 * 2**0) + (c_1 * 2**1) + (c_2 * 2**2) + ... + (c_(k-1) * 2**(k-1))
    # where c_0, c_1, c_2, ..., c_(k-1) belong to {0, 1}
    x = ""

    for i in range(1, k+1):
        val = pow(y, 2**(k-i), p)
        if val == 1:
            # val == 1 ==> c_i == 0 (Euler's Theorem)
            # digit = c_i
            digit = 0
            x += "0"
            # y  =  y*(g**(-c_i*(2**i)) % p) % p  =  y*(g**0 % p) % p  =  y % p
            y = y
        elif val == p-1:
            # val == p-1 ==> c_i == 1
            # digit = c_i
            digit = 1
            x += "1"
            # We need to calculate y  =  y*(g**(-c_i*(2**i)) % p) % p
            # Computed using Step-1 and Step-2
            # Step-1: multiplier = g**(2**(i-1)) % p
            multiplier = pow(g, digit*(2**(i-1)), p)
            # To calculate inverse of `multiplier` mod p, their GCD should be equal to 1
            if GCD(multiplier, p) != 1:
                print "[-] GCD != 1, inverse cannot be calculated. Check your code!"
                return -1
            # Step-2: y = y*(g**(-2**(i-1)) % p) % p
            y = (y*inverse(multiplier, p)) % p
        else:

            print "[-] Some error encountered! Check your code!"
            return -1
    # Values of c_i are appended to `x` in reverse order
    return int(x[::-1], 2)

if __name__ == "__main__":
    try:
        assert pow(3, pohlig_hellman_p2(3, 188, 257, 8), 257) == 188
        assert pow(3, pohlig_hellman_p2(3, 46777, 65537, 16), 65537) == 46777
    except:
        print "[-] Function implementation incorrect!"
