from Crypto.Util.number import *

def crt(list_a, list_m):
    try:
        assert len(list_a) == len(list_m)
    except:
        print "[+] Length of list_a should be equal to length of list_m"
        return -1
    for i in range(len(list_m)):
        for j in range(len(list_m)):
            if GCD(list_m[i], list_m[j])!= 1 and i!=j:
                print "[+] Moduli should be pairwise co-prime"
                return -1
    M = 1
    for i in list_m:
        M *= i
    list_b = [M/i for i in list_m]
    assert len(list_b) == len(list_m)
    try:
        assert [GCD(list_b[i], list_m[i]) == 1 for i in range(len(list_m))]
        list_b_inv = [int(inverse(list_b[i], list_m[i])) for i in range(len(list_m))]
    except:
        print "[+] Encountered an unusual error while calculating inverse using gmpy2.invert()"
        return -1
    x = 0
    for i in range(len(list_m)):
        x += list_a[i]*list_b[i]*list_b_inv[i]
    return x % M

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
    try:
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

def pohlig_hellman(g, y, p, list_q, list_e):
    x_list = [pohlig_hellman_pp(g, y, p, list_q[i], list_e[i]) for i in range(len(list_q))]
    mod_list = [list_q[i]**list_e[i] for i in range(len(list_q))]
    return crt(x_list, mod_list)

if __name__ == "__main__":
    p = 0xfffffed83c17
    print pohlig_hellman(5, 230152795807443, p, [2, 3, 7, 13, 47, 103, 107, 151], [1, 2, 1, 4, 1, 1, 1, 1])
