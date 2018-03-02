'''-----------------------------<Server-Side>-------------------------------'''
from Crypto.Util.number import *
from Crypto.Cipher import AES

# Secret values not known to the attacker
from key import AES_key, MAC_flag

AES_key = AES_key.decode("hex")
iv = "\x00" * 16
BLOCKSIZE = 16

def MAC_generation(plaintext):
	try:
		assert len(plaintext) % 16 == 0
		
		# Does not allow to generate MAC of the below plaintext
		if plaintext == "Check length extension attack!!!":
			print("Not allowed to calculate MAC of this string!")
			exit()

		obj1 = AES.new(AES_key, AES.MODE_CBC, iv)
		ciphertext = obj1.encrypt(plaintext)
		ciphertext = ciphertext[len(ciphertext) - 16:]

		return ciphertext.encode("hex")
	except:
		print "Invalid Input"

def MAC_authentication(auth_tag):
	if auth_tag == MAC_flag:
		print "Successful Exploit!"
	else:
		print "Exploit Failed!"
'''----------------------------</Server-Side>--------------------------------'''

'''---------------------------<Attacker-Side>--------------------------------'''
def xor_strings(s1, s2):
	assert len(s1) == len(s2)
	ct = "".join([chr(ord(s1[i]) ^ ord(s2[i])) for i in range(len(s1))])
	return ct


def exploit():
	target_string = "Check length extension attack!!!"
	assert len(target_string) == 32

	'''Direct Check: Calling the MAC_generation function by passing
	target_string as the parameter directly --> Not allowed by the server'''
	MAC_generation(target_string)

	# Exploit to bypass the plaintext check filter
	print "\n\nThe exploit!!"
	first_slice = target_string[:16]

	'''We are allowed to give input to the server, hence calling the
	MAC_generation function for illustration'''
	MAC_first_slice = MAC_generation(first_slice).decode("hex")
	# MAC_target_string = MAC(MAC(target_string[:16]) xor target_string[16:32])
	second_slice = xor_strings(MAC_first_slice, target_string[16:32])
	MAC_target_string = MAC_generation(second_slice)
	# Calling the MAC_authentication function to illustrate authentication
	MAC_authentication(MAC_target_string)

if __name__ == '__main__':
	exploit()
'''---------------------------</Attacker-Side>-------------------------------'''
