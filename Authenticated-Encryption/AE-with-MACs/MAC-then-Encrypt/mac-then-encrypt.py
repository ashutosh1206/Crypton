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
	return auth_tag.encode("hex")

def cbc_mac_auth(input_str, iv, mac_key, blocksize, auth_tag):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(mac_key, AES.MODE_CBC, iv)
	chk_tag = obj1.encrypt(input_str)[-blocksize:]
	if chk_tag == auth_tag:
		print "Verification Successful"
		return 1
	else:
		print "Verification Failed"
		return 0

def encrypt(input_str, iv, key, blocksize):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = obj1.encrypt(input_str)
	return ciphertext.encode("hex")

def decrypt(ciphertext, iv, key, blocksize):
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	plaintext = obj1.decrypt(ciphertext)
	return unpad(plaintext)

def mac_then_encrypt(input_str, iv, key, mac_key, blocksize):
	tag = cbc_mac_gen(input_str, iv, mac_key, blocksize)
	tag = tag.decode("hex")
	plaintext = input_str + ":" + tag
	ciphertext = encrypt(plaintext, iv, key, blocksize)
	return iv.encode("hex") + ":" + ciphertext

def auth_check(cookie, iv, key, mac_key, blocksize):
	iv, ciphertext = cookie.split(":")
	iv = iv.decode("hex")
	ciphertext = ciphertext.decode("hex")
	plaintext = decrypt(ciphertext, iv, key, blocksize)
	input_str, auth_tag = plaintext.split(":")
	if cbc_mac_auth(input_str, iv, mac_key, blocksize, auth_tag):
		print "Plaintext: ", input_str
	else:
		return "Verification failed, so nothing for you"

str1 = mac_then_encrypt("testplaintext", iv, key, mac_key, blocksize)
print str1
print auth_check(str1, iv, key, mac_key, blocksize)