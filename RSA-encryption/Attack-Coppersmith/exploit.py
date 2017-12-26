from sage.all import *

# f is the monic polynomial f(x) = (m + x)**e - c whose roots we have to find
def stereotyped(f, N):
    P.<x> = PolynomialRing(Zmod(N))
    beta = 1
    dd = f.degree()   # Degree of the polynomial
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    rt = f.small_roots(XX, beta, epsilon)
    return rt

def N-factorize(f, N):
    P.<x> = PolynomialRing(Zmod(N))
    beta = 0.5
    dd = f.degree()    # Degree of the polynomial
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    rt = f.small_roots(XX, beta, epsilon)
    return rt
