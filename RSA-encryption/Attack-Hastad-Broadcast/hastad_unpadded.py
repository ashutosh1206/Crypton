#!/usr/bin/env python2.7
from Crypto.Util.number import GCD, bytes_to_long, long_to_bytes
import gmpy2

def crt(list_a, list_m):
    """
    Reference: https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
    Returns the output after computing Chinese Remainder Theorem on

    x = a_1 mod m_1
    x = a_2 mod m_2
    ...
    x = a_n mod m_n

    input parameter list_a = [a_1, a_2, ..., a_n]
    input parameter list_m = [m_1, m_2, ..., m_n]

    Returns -1 if the operation is unsuccessful due to some exceptions
    """
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
        list_b_inv = [int(gmpy2.invert(list_b[i], list_m[i])) for i in range(len(list_m))]
    except:
        print "[+] Encountered an unusual error while calculating inverse using gmpy2.invert()"
        return -1
    x = 0
    for i in range(len(list_m)):
        x += list_a[i]*list_b[i]*list_b_inv[i]
    return x % M


def test_crt():
    """
    Checking the validity and consistency of CRT function
    """
    list_a = [[2, 3], [1, 2, 3, 4], [6, 4]]
    list_m = [[5, 7], [5, 7, 9, 11], [7, 8]]
    soln_list = [17, 1731, 20]
    try:
        for i in range(len(list_a)):
            assert crt(list_a[i], list_m[i]) == soln_list[i]
    except:
        print "[+] CRT function broken. Check the function again!"


def hastad_unpadded(ct_list, mod_list, e):
    """
    Implementing Hastad's Broadcast Attack
    """
    m_expo = crt(ct_list, mod_list)
    if m_expo != -1:
        eth_root = gmpy2.iroot(m_expo, e)
        if eth_root[1] == False:
            print "[+] Cannot calculate e'th root!"
            return -1
        elif eth_root[1] == True:
            return long_to_bytes(eth_root)
    else:
        print "[+] Cannot calculate CRT"
        return -1

test_crt()
