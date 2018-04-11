from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from hashlib import md5

def signer(M):
	message = M
	p = getPrime(512)
	q = getPrime(512)
	n = p*q
	phin = (p-1)*(q-1)
	e = 65537
	key = RSA.construct((long(n), long(e)))
	assert GCD(e, phin) == 1
	d = inverse(e, phin)
	M = md5(M).digest()
	M = bytes_to_long(M)
	s = pow(M, d, n)
	s = long_to_bytes(s)
	return (key, s, message)

def verifier(pubkey, s, M):
	s = bytes_to_long(s)
	n = pubkey.n
	e = pubkey.e
	M = md5(M).digest()
	pt = pow(s, e, n)
	pt = long_to_bytes(pt)
	if pt == M:
		print "Verified!"
	else:
		raise VerificationError("Verification Failed!")

M = "testing"
pubkey, s, M = signer(M)
verifier(pubkey, s, M)