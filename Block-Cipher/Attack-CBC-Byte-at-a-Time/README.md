# CBC Byte at a Time Attack
  
Prerequisites:  
1. [Block Ciphers](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher)
2. [CBC mode of encryption](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Mode-of-Encryption)
3. [ECB Byte at a time Attack](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-ECB-Byte-at-a-Time)

The attack is almost similar too, and the exploit script will also be the same in both cases. They only differ in their computations, since in CBC mode plaintext is XORed with the ciphertext of the previous block, but we don't have to worry about it in our attack, since the server does the job.  
Check out an example for this attack [here](exploit.py)
  
# References
1. [Byte wise decryption of AES-CBC by grocid](https://grocid.net/2016/05/01/byte-wise-decryption-of-aes-cbc/)
