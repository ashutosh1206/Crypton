from sage.all import *

def wiener(e, n):
	m = 12345
	c = pow(m, e, n)
	q0 = 1

	list1 = continued_fraction(Integer(e)/Integer(n))
	conv = list1.convergents()
	for i in conv:
		k = i.numerator()
		q1 = i.denominator()

		for r in range(30):
			for s in range(30):
				d = r*q1 + s*q0
				m1 = pow(c, d, n)
				if m1 == m:
					return d
		q0 = q1
        return None