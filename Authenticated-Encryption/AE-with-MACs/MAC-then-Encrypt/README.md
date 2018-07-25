# MAC-then-Encrypt
  
Prerequisites:
1. [Message Authentication Code](../../../Message-Authentication-Code/)
  
  

In this article we will:
1. Discuss Authenticated Encryption using MAC-then-Encrypt technique
2. Implement a simple Authenticated Encryption service using MAC-then-Encrypt technique
  
  

This method of authenticated encryption using MACs is slightly different from Encrypt-and-MAC technique. In this technique, only one entity is sent over the communication channel and that is the ciphertext. The ciphertext itself is generated from the plaintext and the authentication tag, we will see the internals in coming sections. 
  
As mentioned before, keys used for encryption and for generating MAC must be different.  
  
To understand MAC-then-Encrypt clearly, have a look at this illustration from Wikipedia:  
![picture](https://i.imgur.com/ZyeSVPR.png)  
  

## Sending messages securely using MAC-then-Encrypt
Consider Alice as the sender and Bob as the receiver. Bob will not only decrypt the message and read it, but also check if the authenticated tag of the message received is equal to the authentication tag received. The message is accepted by Bob only if this condition holds true. To send a message through MAC-then-Encrypt technique:  
1. Assuming the message to be sent is `M`, Alice computes it's corresponding authenticated tag `T` as:
   + ![picture](Pictures/1.png), where `k2` is the key used to generate the authentication tag. Note that key is not known to the attacker.
     + Also, the mechanism of this technique is not affected by the type of the algorithm used to generate the authentication tag. Alice can used either a Hash based MAC or block cipher modes such as CBC mode to compute the authentication tag.
     + Alice must make sure that the algorithm is secure enough and authentication tag does not reveal any information about the plaintext.
2. Next, Alice concatenates message `M` and it's authentication tag `T`, pads it to make it a multiple of the block size and encrypts the resultant string using a secure block cipher algorithm (AES etc.) to generate ciphertext `C`
   + ![picture](Pictures/2.png), where `k1` is the key used to generate the ciphertext.
3. Alice then sends this ciphertext through the communication channel to Bob.

Implementation of the steps described above:  
```python
def encrypt(input_str, iv, key, blocksize):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	ciphertext = obj1.encrypt(input_str)
	return ciphertext.encode("hex")

def cbc_mac_gen(input_str, iv, mac_key, blocksize):
	input_str = pad(input_str, blocksize)
	obj1 = AES.new(mac_key, AES.MODE_CBC, iv)
	auth_tag = obj1.encrypt(input_str)[-blocksize:]
	return auth_tag.encode("hex")

def mac_then_encrypt(input_str, iv, key, mac_key, blocksize):
	tag = cbc_mac_gen(input_str, iv, mac_key, blocksize)
	tag = tag.decode("hex")
	plaintext = input_str + ":" + tag
	ciphertext = encrypt(plaintext, iv, key, blocksize)
	return iv.encode("hex") + ":" + ciphertext
```
  
  

## Authentication through MAC-then-Encrypt
After receiving Alice's message, Bob does the following:  
1. Decrypts the ciphertext `C` using key `k1`:
   + ![picture](Pictures/3.png)
2. Bob now has the decrypted ciphertext. As we know that the plaintext obtained is a concatenation of message `M` and authentication `T`. Bob now separates `M` and `T` and also checks if MAC of the message obtained is equal to the authentication tag `T`:  
   + ![picture](Pictures/4.png)
   + If the tags match, then `M` will be accepted and an acknowledge will be sent to Alice. Otherwise, a VerificationError will be generated.

Implementation of the above verification steps: 
```python
def decrypt(ciphertext, iv, key, blocksize):
	obj1 = AES.new(key, AES.MODE_CBC, iv)
	plaintext = obj1.decrypt(ciphertext)
	return unpad(plaintext)

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
```
  
  
You can check out the entire example script for MAC-then-Encrypt technique [here](mac-then-encrypt.py)

## References
1. [Authenticated Encryption- Wikipedia](https://en.wikipedia.org/wiki/Authenticated_encryption)

