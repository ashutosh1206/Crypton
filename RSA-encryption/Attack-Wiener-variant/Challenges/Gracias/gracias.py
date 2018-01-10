#!/usr/bin/python

from gmpy import *
from Crypto.Util.number import *
import gensafeprime    
from flag import FLAG

def make_pubpri(nbit):
    p, q, r = [ getPrime(nbit) for _ in xrange(3)]
    n = p * q * r
    phi = (p-1)*(q-1)*(r-1)
    l = min([p, q, r])
    d = getPrime(1 << 8)
    e = inverse(d, phi)
    a = gensafeprime.generate(2*nbit)
    while True:
        g = getRandomRange(2, a)
        if pow(g, 2, a) != 1 and pow(g, a/2, a) != 1:
            break
    return (n, e, a, g), (n, d, a, g)

def encrypt(m, pub):
    n, e, a, g = pub
    k = getRandomRange(2, a)
    K = pow(g, k, a)
    c1, c2 = pow(k, e, n), (m * K) % a
    return c1, c2

nbit = 512
pubkey, privkey = make_pubpri(nbit)
m = bytes_to_long(FLAG)
c = encrypt(m, pubkey)
print 'c =', c
print 'pubkey =', pubkey