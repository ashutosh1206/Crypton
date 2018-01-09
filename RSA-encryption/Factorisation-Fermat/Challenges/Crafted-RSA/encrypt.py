from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
import random
from secret import num_size

seed = 0

def genPrime(sz):
    global seed
    while True:
        if seed == 0:
            pr = getPrime(sz)
            while size(pr) < 1024:
                pr *= getRandomNBitInteger(16)
            i = 2
            while i<1000 and size(pr)==1024:
                if isPrime(pr+i) and size(pr+i) == 1024:
                    seed = pr+i
                    return pr+i
                i += 1
        else:
            pr = seed + random.randint(2**100,2**300)
            if isPrime(pr) and size(pr) == 1024:
                seed = pr
                return pr

p = genPrime(num_size)
q = genPrime(num_size)
e = 2**16 + 1
phin = (p-1)*(q-1)
n = p*q

print "n: ", n
print "p: ", p
print "q: ", q

flag = open("flag.txt", 'r').read()
flag = int(flag.encode("hex"),16)

ciphertext = hex(pow(flag, e, n))[2:].replace("L","")
print ciphertext
obj1 = open("ciphertext.txt", 'w').write(ciphertext)
