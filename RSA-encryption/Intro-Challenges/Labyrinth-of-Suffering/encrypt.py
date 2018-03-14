from Crypto.Util.number import *
from Crypto.PublicKey import *
import gmpy2
from secret import flag

p = getPrime(512)
q = getPrime(512)
n = p*q
e = 65537

s = pow(2, p-0xdeadbeef, n)
message = bytes_to_long(flag)
ciphertext = pow(message, e, n)
ciphertext = long_to_bytes(ciphertext)
ciphertext = ciphertext.encode("hex")

out_str = "[1] ciphertext: " + ciphertext + "\n[2] n: " + str(n) + "\n[3] e: " + str(e) + "\n[4] s: " + str(s)
obj1 = open("data.txt",'w')
obj1.write(out_str)