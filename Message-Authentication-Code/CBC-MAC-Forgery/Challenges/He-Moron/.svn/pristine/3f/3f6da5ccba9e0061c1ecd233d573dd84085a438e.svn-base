def sign(k, m):
	ECB = AES.new(k, AES.MODE_ECB)
	mb = [m[i:i + 16] for i in range(0, len(m), 16)]
	t = ECB.encrypt(mb[0])
	for i in range(1,len(mb)):
	    t = ECB.encrypt(strxor(mb[i], t))
	return hexlify(t)
