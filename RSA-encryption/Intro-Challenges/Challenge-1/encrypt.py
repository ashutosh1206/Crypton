from Crypto.Util.number import *
from Crypto.PublicKey import RSA
from secret import flag
import gmpy2

"""
pycrypto documentation: https://www.dlitz.net/software/pycrypto/api/2.6/
gmpy2 documentation [OPTIONAL]: https://gmpy2.readthedocs.io/en/latest/
"""

# (e, n) together is known as the public key, e is known as the public key exponent, n is known as the modulus
# (d, n) together is known as the private key, d is known as the private key exponent, n is known as the modulus

"""
secret values (these are not known to the attacker): d, p, q
public values: e, n
"""

# p, q are two primes of size 512 bits
# The following pycrypto commands have been used to generate primes of size 512 bits: p = getPrime(512), q = getPrime(512)
p = 6958271393287170117448891021448827870244652620796166337874899406278127643022124226656230972235829204217718701711355755622520840943962368410353060326959627L
q = 10816988558466468069802205154113557859050665172995721741674476865844313409030354507360669179381457836401919224815040955096510785560864262908230559354811907L

# n = p*q, n is known as the modulus
n = p*q
e = 65537

phin = (p-1)*(q-1)
""" 
Modular inverse c = a^(-1) mod b can be calculated only when GCD(a, b) == 1
Hence, the command below checks the same before calculating modular inverse 
Want to know why we check GCD(a, b) before calculating the modular inverse? You can refer the following links: 
1. Geeks for Geeks:   https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
2. Wolfram MathWorld: http://mathworld.wolfram.com/ModularInverse.html
3. Wikipedia:         https://en.wikipedia.org/wiki/Modular_multiplicative_inverse
""" 
assert GCD(e, phin) == 1
# Have a look documentation of gmpy2 and usage of various functions of gmpy2 before moving forward [OPTIONAL]: https://gmpy2.readthedocs.io/en/latest/
# Calculating the modular inverse d = e^(-1) mod phin
# Note that d is only used for decryption and this script is used to encrypt the message.
# The command below is only used to illustrate how d is calculated.
d = inverse(e, phin)
# You can also use gmpy2's invert(e, phin) to get d


# Transforming a string to a long integer using pycrypto's function bytes_to_long() in Crypto.Util.number
# m is the message to be encrypted
m = bytes_to_long(flag)


# ciphertext = m^e mod n
ciphertext = pow(m, e, n)
# converting the ciphertext from long integer to string using long_to_bytes() in Crypto.Util.number
ciphertext = long_to_bytes(ciphertext)
obj1 = open("ciphertext.txt",'w')
obj1.write(ciphertext.encode("hex"))