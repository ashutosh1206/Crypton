from Crypto.Util.number import *
import hashlib
import random

def key_gen(bit_size):
	p = getPrime(bit_size)
	g = 2
	x = random.randint(2, p-3)
	y = pow(g, x, p)
	return (y, p, g)

def sign(message, y, p, g):
	h = hashlib.md5(message).hexdigest()
	while True:
		k = random.randint(2, p-2)
		if GCD(k, p-1) == 1:
			break
	r = pow(g, k, p)
	s = ((h-(x*r))*inverse(k, p-1)) % (p-1)
	return (r, s, message)

def verify(message, s, r, y, p, g):
	try:
		assert r > 0 and r < p
		assert s > 0 and s < p-1
		h = hashlib.md5(message).hexdigest()
		assert pow(g, h, p) == (pow(r, s, p)*pow(y, r, p)) % p
		print "Signature successfully verified!"
	except:
		raise VerificationError("Invalid Signature!")
