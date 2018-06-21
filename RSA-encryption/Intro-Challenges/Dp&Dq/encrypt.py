from Crypto.Util.number import *
import gmpy2
from Crypto.PublicKey import RSA
from secret import flag, factor_p, factor_q

n = 78947048749078921553533397168223306327077414586183944609818553584663665747677757164091069731707888197818123265891690348381736231229561730395657333262905613958377739828118875586000068815867354664296956931106342366972209987312006882239420435532019823504851246162228112328268031305782869824549589268029030234941
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