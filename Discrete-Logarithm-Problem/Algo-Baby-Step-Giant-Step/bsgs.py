from sage.all import *

def bsgs(g, y, p):
    """
    Reference:

    To solve DLP: y = g^x % p and get the value of x.
    We use the property that x = i*m + j, where m = ceil(sqrt(n))

    :parameters:
        g : int/long
                Generator of the group
        y : int/long
                Result of g**x % p
        p : int/long
                Group over which DLP is generated. Commonly p is a prime number

    :variables:
        m : int/long
                Upper limit of baby steps / giant steps
        x_poss : int/long
                Values calculated in each giant step
        c : int/long
                Giant Step pre-computation: c = g^(-m) % p
        i, j : int/long
                Giant Step, Baby Step variables
        lookup_table: dictionary
                Dictionary storing all the values computed in the baby step
    """
    mod_size = len(bin(p-1)[2:])

    print "[+] Using BSGS algorithm to solve DLP"
    print "[+] Modulus size: " + str(mod_size) + ". Warning! BSGS not space efficient\n"

    m = ceil(sqrt(p-1))
    # Baby Step
    lookup_table = {pow(g, j, p): j for j in range(m)}
    # Giant Step pre-computation
    c = pow(g, m*(p-2), p)
    # Giant Steps
    for i in range(m):
        temp = (y*pow(c, i, p)) % p
        if temp in lookup_table:
            # x found
            return i*m + lookup_table[temp]
    return None


if __name__ == "__main__":
    try:
        assert pow(2, bsgs(2, 4178319614, 6971096459), 6971096459) == 4178319614
        assert pow(3, bsgs(3, 362073897, 2500000001), 2500000001) == 362073897
    except:
        print "[+] Function inconsistent and incorrect, check the implementation"
