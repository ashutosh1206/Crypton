from Crypto.Util.number import *
import random

def generate_key(size):
	p = getPrime(size)
	x = random.randint(2, p-2)
	g = 2
	h = pow(g, x, q)
	return (h, g, q)

def encrypt(message, h, g, q):
	message = bytes_to_long(message)
	y = random.randint(2, p-2)
	c1 = pow(g, y, q)
	s = pow(h, y, q)
	c2 = (m*s) % q
	return (c1, c2)

def decrypt(c1, c2, g, q, x):
	s = pow(c1, x, q)
	m = (c2*inverse(s, q)) % q
	return m