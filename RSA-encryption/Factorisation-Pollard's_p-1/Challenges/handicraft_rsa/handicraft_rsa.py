#!/usr/bin/python

from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from secret import s, FLAG

def gen_prime(s):
    while True:
        r = getPrime(s)
        R = [r]
        t = int(5 * s / 2) + 1
        for i in range(0, t):
            R.append(r + getRandomRange(0, 4 * s ** 2))
        p = reduce(lambda a, b: a * b, R, 2) + 1
        if isPrime(p):
            if len(bin(p)[2:]) == 1024:
                return p

while True:
    p = gen_prime(s)
    q = gen_prime(s)
    n = p * q
    e = 65537
    d = inverse(e, (p-1)*(q-1))
    if len(bin(n)[2:]) == 2048:
        break

msg = FLAG
key = RSA.construct((long(n), long(e), long(d), long(p), long(p)))
for _ in xrange(s):
    enc = key.encrypt(msg, 0)[0]
    msg = enc

print key.publickey().exportKey()
print '-' * 76
print enc.encode('base64')
print '-' * 76
