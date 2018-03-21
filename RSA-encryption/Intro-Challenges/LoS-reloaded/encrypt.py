from Crypto.Util.number import *
import hashlib
import gmpy2

p = getPrime(512)
q = getPrime(512)
n = p*q
print "n: ", n
e = 65537
d = inverse(e, (p-1)*(q-1))
print "d: ", d

hash_p = hashlib.sha256(str(p)).hexdigest()
hash_q = hashlib.sha256(str(q)).hexdigest()


# You only have access to the variables being printed on the screen when you run this program
print "You have two chances to get out of this labyrinth: "
for i in range(2):
	p1 = raw_input("Give me p: ")
	p2 = raw_input("Give me q: ")
	if hashlib.sha256(p1).hexdigest() == hash_p and hashlib.sha256(p2).hexdigest() == hash_q:
		print "Nice, you solved it. But how do you get of the labyrinth of suffering?? Getting out of it isn't easy"
		print "You still feel trapped, don't you?"
		break
	else:
		print "Oops sorry"