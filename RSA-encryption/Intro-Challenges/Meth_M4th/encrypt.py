from Crypto.Util.number import *
from Crypto.PublicKey import RSA
import gmpy2
from secret import flag

p = getPrime(512)
q = getPrime(512)
n = p*q
phin = (p-1)*(q-1)

s = p*(n-p-q+1)
e = 65537
assert GCD(e, phin) == 1
d = inverse(e, phin)

message = bytes_to_long(flag)
ciphertext = pow(message, e, n)
ciphertext = long_to_bytes(ciphertext)
ciphertext = ciphertext.encode("hex")

obj1 = open("data.txt",'w')
write_data = "[1] Ciphertext: " + ciphertext + "\n" + "[2] Modulus: " + str(n) + "\n" + "[3] Public Key exponent: " + str(e) + "\n" + "[4] s: " + str(s)
obj1.write(write_data)
obj1.close()