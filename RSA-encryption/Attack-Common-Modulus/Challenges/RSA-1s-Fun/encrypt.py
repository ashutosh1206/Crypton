from Crypto.Util.number import *

e1 = 9
e2 = 123

def prime_gen():
    while True:
        p = getPrime(1024)
        q = getPrime(1024)
        n = p*q
        phin = (p-1)*(q-1)
        if GCD(e1, phin) == 1 and GCD(e2, phin) == 1:
            return (p, q, n)
p, q, n = prime_gen()

print "p: ", p
print "q: ", q
print "n: ", n

flag = bytes_to_long(open("flag.txt").read().strip())
assert flag < n
assert flag**9 > n

c1 = pow(flag, e1, n)
c2 = pow(flag, e2, n)

print "c1: ", c1
print "c2: ", c2
