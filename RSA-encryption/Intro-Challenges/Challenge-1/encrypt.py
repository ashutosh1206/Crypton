from Crypto.Util.number import *
import gmpy2
from secret import flag

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537

# Euler's Totient function
phin = (p-1)*(q-1)
assert GCD(e, phin)
# Private key exponent
d = inverse(e, phin)

# m is the message/flag
m = bytes_to_long(flag)
ciphertext = pow(m, e, n)
ciphertext = long_to_bytes(ciphertext).encode("hex")
print "d: ", d
print "ciphertext: ", ciphertext


# Writing private key to privatekey.txt
obj1 = open("privatekey.txt",'w')
append = "d: " + str(d) + "\n" + "n: " + str(n)
obj1.write(append)
obj1.close()

obj1 = open("ciphertext.txt",'w')
obj1.write(ciphertext)
obj1.close()