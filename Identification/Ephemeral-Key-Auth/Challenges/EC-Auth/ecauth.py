#!/usr/bin/env python2.7

# Class for declaring an Elliptic Curve of the form y^2 = x^3 + ax + b (mod p)
class CurveFp( object ):
    def __init__( self, p, a, b ):
        """
        Declaring values of parameters `a`, `b`, `p` in the Elliptic Curve- y^2 = x^3 + ax + b (mod p)
        """
    	self.__p = p
    	self.__a = a
    	self.__b = b

    def p( self ):
	       return self.__p

    def a( self ):
	       return self.__a

    def b( self ):
	       return self.__b

    def contains_point( self, x, y ):
        """
        To check whether a point (x, y) lies on the Elliptic Curve y^2 = x^3 + ax + b (mod p):
        verify if y^2 - (x^3 + ax + b) is a multiple of p,
        return True if the condition holds true,
        return False if it doesn't
        """
        return ( y * y - ( x * x * x + self.__a * x + self.__b ) ) % self.__p == 0

# Testing code for CurveFp Class
def testCurveFp():
	p = 89953523493328636138979614835438769105803101293517644103178299545319142490503L
	a = 89953523493328636138979614835438769105803101293517644103178299545319142490500
	b = 28285296545714903834902884467158189217354728250629470479032309603102942404639
	objtest = CurveFp(p, a, b)

	Gx = 0x337ef2115b4595fbd60e2ffb5ee6409463609e0e5a6611b105443e02cb82edd8L
	Gy = 0x1879b8d7a68a550f58166f0d6b4e86a0873d7b709e28ee318ddadd4ccf505e1aL

	Qx = 0x2a40fd522f73dc9f7c40b2420e39e62c5742ff2f11805a1577ed7f60153a0be1L
	Qy = 0x3085e99246006b71b4211eff47ff3efc0f93103ee7379dc3bcc6decdc46073a3L

	Rx = 0xbd0a442367bdc24cb09c49404e3d307ba99122e7b78e14f0d84870d0df97aa59L
	Ry = 0x22c88612db6b6af6f196cd815fc5f57fe871d3b6588b0c7a59e06cc759d736b2L
	assert objtest.contains_point(Gx, Gy) == True
	assert objtest.contains_point(Qx, Qy) == True
	assert objtest.contains_point(Rx, Ry) == True

class Point( object ):
    def __init__( self, curve, x, y, order = None ):
        self.__curve = curve
        self.__x = x
        self.__y = y
        self.__order = order
        if self.__curve:
            assert self.__curve.contains_point( x, y )
        if order:
            assert self * order == INFINITY

    def __add__( self, other ):
        if other == INFINITY: return self
        if self == INFINITY: return other
        assert self.__curve == other.__curve
        if self.__x == other.__x:
            if ( self.__y + other.__y ) % self.__curve.p() == 0:
                return INFINITY
            else:
                return self.double()

        p = self.__curve.p()
        l = ( ( other.__y - self.__y ) * inverse_mod( other.__x - self.__x, p ) ) % p
        x3 = ( l * l - self.__x - other.__x ) % p
        y3 = ( l * ( self.__x - x3 ) - self.__y ) % p
        return Point( self.__curve, x3, y3 )

    def __mul__( self, other ):
        def leftmost_bit( x ):
            assert x > 0
            result = 1L
            while result <= x: result = 2 * result
            return result / 2

        e = other
        if self.__order: e = e % self.__order
        if e == 0: return INFINITY
        if self == INFINITY: return INFINITY
        assert e > 0
        e3 = 3 * e
        negative_self = Point( self.__curve, self.__x, -self.__y, self.__order )
        i = leftmost_bit( e3 ) / 2
        result = self
        while i > 1:
            result = result.double()
            if ( e3 & i ) != 0 and ( e & i ) == 0: result = result + self
            if ( e3 & i ) == 0 and ( e & i ) != 0: result = result + negative_self
            i = i / 2
        return result

    def __rmul__( self, other ):
        return self * other

    def __str__( self ):
        if self == INFINITY: return "infinity"
        return "(%d,%d)" % ( self.__x, self.__y )

    def double( self ):
        if self == INFINITY:
            return INFINITY

        p = self.__curve.p()
        a = self.__curve.a()
        l = ( ( 3 * self.__x * self.__x + a ) * inverse_mod( 2 * self.__y, p ) ) % p
        x3 = ( l * l - 2 * self.__x ) % p
        y3 = ( l * ( self.__x - x3 ) - self.__y ) % p
        return Point( self.__curve, x3, y3 )

    def x( self ):
        return self.__x

    def y( self ):
        return self.__y

    def curve( self ):
        return self.__curve

    def order( self ):
        return self.__order

INFINITY = Point( None, None, None )

def inverse_mod( a, m ):
    if a < 0 or m <= a: a = a % m
    c, d = a, m
    uc, vc, ud, vd = 1, 0, 0, 1
    while c != 0:
        q, c, d = divmod( d, c ) + ( c, )
        uc, vc, ud, vd = ud - q*uc, vd - q*vc, uc, vc
    assert d == 1
    if ud > 0: return ud
    else: return ud + m

class Handshake(object):
    def __init__(self, Q, R, s):
        self.Q = Q
        self.R = R
        self.s = s

class Public_key(object):
    def __init__(self, generator):
        self.generator = generator
        self.curve = generator.curve()
        n = generator.order()
        if not n:
            raise RuntimeError("Generator must have order")
        if not n * generator == INFINITY:
            raise RuntimeError("Generator point order is bad")
        if generator.x() < 0 or n <= generator.x() or  generator.y() < 0 or n <= generator.y():
            raise RuntimeError("Generator point has x or y out of range")

    def check(self, point):
        k = self.generator.order()
        if not k:
            raise RuntimeError("Generator must have order")
        if not k * point == INFINITY:
            raise RuntimeError("Generator point order is bad")
        if point.x() < 0 or k <= point.x() or  point.y() < 0 or k <= point.y():
            raise RuntimeError("Generator point has x or y out of range")

    def _verify(self, handshake):
        P = self.generator
        Q = handshake.Q
        R = handshake.R
        s = handshake.s
        try:
            self.check(Q)
            self.check(R)
        except:
            return False
        if (s*P).x() == (Q+R).x() and (s*P).y() == (Q+R).y():
            return True
        else:
            return False

class Private_key(object):
    def __init__(self, public_key, x):
        self.public_key = public_key
        self.privkey = x

    def _sign(self, r):
        P = self.public_key.generator
        Q = self.privkey * P
        R = r * P
        s = self.privkey + r
        return Handshake(Q, R, s)
