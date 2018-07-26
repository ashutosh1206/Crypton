"""
An illustration of MAC then Encrypt technique of Authenticated Encryption with MACs
MAC algorithm: CBC-MAC
Encryption: AES in CBC mode
Note that this is only for illustrative purposes (the script is vulnerable to CBC-MAC forgery and more implementation attacks-
even the unpad function is vulnerable!) 
"""

from Crypto.Cipher import AES
from os import urandom
from Crypto.Util.number import *

key = urandom(16)
iv = urandom(16)
mac_key = urandom(16)

blocksize = 16

def pad(input_str, blocksize):
	input_str += chr(blocksize - len(input_str) % blocksize)*(blocksize - len(input_str) % blocksize)
	assert len(input_str) % blocksize == 0
	return input_str

def unpad(input_str):
	return input_str[:-ord(input_str[-1])]

def cbc_mac_gen(input_str, iv, mac_key, blocksize):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(mac_key, AES.MODE_CBC, iv)
	auth_tag = obj1.encrypt(input_str)[-blocksize:]
	return auth_tag

def encrypt(input_str, iv, key, blocksize):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = obj1.encrypt(input_str)
	return ciphertext

def decrypt(ciphertext, iv, key, blocksize):
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	plaintext = obj1.decrypt(ciphertext)
	return unpad(plaintext)

def encrypt_then_mac(input_str, iv, key, mac_key, blocksize):
	ciphertext = encrypt(input_str, iv, key, blocksize)
	tag = cbc_mac_gen(ciphertext, iv, mac_key, blocksize)
	return ciphertext.encode("hex") + ":" + tag.encode("hex")

def auth_check(session_cookie, iv, key, mac_key, blocksize):
	ciphertext, tag = session_cookie.split(":")
	ciphertext = ciphertext.decode("hex")
	tag = tag.decode("hex")
	if cbc_mac_gen(ciphertext, iv, mac_key, blocksize) == tag:
		print "Authentication Successful"
		return decrypt(ciphertext, iv, key, blocksize)
	else:
		print "Authentication Failed"
		return 0

str1 = encrypt_then_mac("testplaintext", iv, key, mac_key, 16)
print str1
print auth_check(str1, iv, key, mac_key, blocksize)