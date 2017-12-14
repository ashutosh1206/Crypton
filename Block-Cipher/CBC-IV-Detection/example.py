from Crypto.Cipher import AES
from os import urandom

key = urandom(16)
iv = urandom(16)

def padding(plaintext, blocksize):
	padlen = blocksize - (len(plaintext) % blocksize)
	pt_hex = plaintext.encode("hex") + padlen*(hex(padlen)[2:].zfill(2))
	return pt_hex.decode("hex")

def CBC_encrypt(plaintext):
	plaintext = padding(plaintext, 16)
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	return obj1.encrypt(plaintext)

def CBC_decrypt(ciphertext):
	obj2 = AES.new(key, AES.MODE_CBC, iv)
	plaintext = obj2.decrypt(ciphertext)
	return plaintext

# Assuming the above code is running on a server and we only have access to its encryption and decryption oracle
# We can do the following, as an attacker to get the value of iv
#----------------------------------------------------------------------------------------------------------------------------------
# The following is what an attacker will do to implement the exploit

plaintext = "Crypton is a repository of a compilation of all the popular attacks on encryption systems and digital signatures"
plaintext = padding(plaintext, 16) # Assuming that the attacker knows blocksize
ciphertext = CBC_encrypt(plaintext)

# For the exploit we need atleast three blocks of ciphertext
ciphertext = ciphertext[:16] + "\x00"*16 + ciphertext[:16]
pt = CBC_decrypt(ciphertext)
possible_iv = ""
for i in range(16):
    possible_iv += chr(ord(pt[i]) ^ ord(pt[32+i]))
print possible_iv == iv

if possible_iv == iv:
    print "[*] Exploit working. The value of iv in hex is: ", possible_iv.encode("hex")
else:
    print "[*] Exploit failed!"
