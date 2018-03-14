from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
from secret import flag


p = getPrime(512)

i = 10000
while True:
	q = p + i
	if isPrime(q):
		break
        i += 1
print "i: ", i
n = p*q
e = 65537
phin = (p-1)*(q-1)
assert GCD(e, phin) == 1

d = inverse(e, phin)

# Message/Flag to be encrypted
m = bytes_to_long(flag)
ciphertext = long_to_bytes(pow(m, e, n))
ciphertext = ciphertext.encode("hex")

obj1 = open("ciphertext.txt",'w')
obj1.write(ciphertext)

key = RSA.construct((n, long(e)))
f = open("publickey.pem",'w')
f.write(key.exportKey("PEM"))