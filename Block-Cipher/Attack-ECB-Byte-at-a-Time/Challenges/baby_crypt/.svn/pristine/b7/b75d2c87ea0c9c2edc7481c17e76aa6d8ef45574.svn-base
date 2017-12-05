#!/usr/bin/python

def dumb_pad(imp):
    while len(imp)%16 != 0:
        imp+="0"
    return imp


from Crypto.Cipher import AES
import hashlib


k = hashlib.sha256()
flag = "flag{Crypt0_is_s0_h@rd_t0_d0...}"
k.update(flag)
key  = k.digest()
c = AES.new(key,AES.MODE_ECB);
def oracle(inp):
    #c = AES.new(key,AES.MODE_ECB);
    return c.encrypt(dumb_pad(inp+flag)).encode('hex')

while True:
    imp = raw_input("Enter your username (no whitespace): ")
    print("Your Cookie is: " + oracle(imp))
