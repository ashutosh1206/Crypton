from Crypto.Util.number import *
import gmpy2
from Crypto.PublicKey import RSA
from secret import flag, factor_p, factor_q

n = 386931010476066075837968435835568572278162262133897268076172926477773222237770106161904290022544637634198443777989318861346776496147456733417801969323559935547762053140311065149570645042679207282163944764258457818336874606186063312212223286995796662956880884390624903779609227558663952294861600483773641805524656787990883017538007871813015279849974842810524387541576499325580716200722985825884806159228713614036698970897017484020439048399276917685918470357385648137307211493845078192550112457897553375871556074252744253633037568961352527728436056302534978263323170336240030950585991108197098692769976160890567250487423
e = 65537

p = factor_p
q = factor_q
assert p*q == n
phin = (p - 1)*(q - 1)

d = inverse(e, phin)

# d congruent to dp (mod p)
# d congruent to dq (mod q)
# Apply Chinese Remainder Theorem to solve the equations and get d
# Ref. to: https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html
# Ref. to: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
dp = d % (p-1)
dq = d % (q-1)

key = RSA.construct((n, long(e)))
obj1 = open("publickey.pem",'w')
obj1.write(key.exportKey('PEM'))
obj1.close()

message = bytes_to_long(flag)
ciphertext = pow(message, e, n)
ciphertext = long_to_bytes(ciphertext)
ciphertext = ciphertext.encode("hex")

f = open("data.txt",'w')
f.write("[*] ciphertext: " + ciphertext + "\n" + "[*] dp: " + str(dp) + "\n" + "[*] dq: " + str(dq))
f.close()
