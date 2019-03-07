param = {   "hacklu":
            ((889774351128949770355298446172353873, 12345, 67890),
            # Generator of Subgroup of prime order 73 bits, 79182553273022138539034276599687 to be excact
            (238266381988261346751878607720968495, 591153005086204165523829267245014771),
            # challenge Q = xP, x random from [0, 79182553273022138539034276599687)
            (341454032985370081366658659122300896, 775807209463167910095539163959068826)
            )
        }

serverAdress = '0.0.0.0'
serverPort = 23426

(p, a, b), (px, py), (qx, qy) = param["hacklu"]
E = EllipticCurve(GF(p), [a, b])
P = E((px, py))
Q = E((qx, qy))

def is_distinguished_point(p):
    return p[0] < 2^(100)
