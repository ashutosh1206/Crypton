#!/usr/bin/env python
from Crypto.PublicKey import *
from Crypto.Util.number import *
import os, sys

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

def _encrypt(message, e, n):
    m = bytes_to_long(message)
    return long_to_bytes(pow(m, e, n))

def _decrypt(ciphertext, d, n):
    ct = bytes_to_long(ciphertext)
    return long_to_bytes(pow(ct, d, n) % 2)

def genkey(size):
    p = getPrime(size/2)
    q = getPrime(size/2)
    e = 65537
    phin = (p-1)*(q-1)
    d = inverse(e, phin)
    n = p*q
    return (p, q, e, d, phin, n)

if __name__ == "__main__":
    p, q, e, d, phin, n = genkey(1024)
    # Make any flag file to run this challenge
    flag = open("flag").read().strip()
    print "Welcome to RSA encryption oracle!"
    print "Here take your flag (in hex): ", _encrypt(flag, e, n).encode("hex")
    print "Here take modulus: ", n
    for i in range(1050):
        print "RSA service"
        print "[1] Encrypt"
        print "[2] Decrypt"
        option = int(raw_input("Enter your choice: "))
        if option == 1:
            try:
                print "Coming here"
                message = raw_input("Enter the message you want to encrypt (in hex): ").decode("hex")
            except:
                print "Enter proper hex chars"
                exit(0)
            ct = _encrypt(message, e, n)
            print "Here take your ciphertext (in hex): ", ct.encode("hex")
            print "\n\n"
        elif option == 2:
            try:
                ciphertext = raw_input("Enter the ciphertext you want to decrypt (in hex): ").decode("hex")
            except:
                print "Enter proper hex chars"
                exit(0)
            msg = _decrypt(ciphertext, d, n)
            print "Here take your plaintext (in hex): ", msg.encode("hex")
            print "\n\n"
        else:
            print "Enter a valid option!"
    print "Exiting..."
