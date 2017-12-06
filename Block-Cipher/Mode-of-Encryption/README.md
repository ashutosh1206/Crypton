# Mode of encryption
A block cipher takes in a block of data of size equal to the blocksize, a key (and an IV in some cases). The algorithm does not know of how encryption of each block of data affects the blocks present next to it. This is in fact governed by the mode in which the data is encrypted in a block cipher.

Prerequisite:
1. Block Cipher
2. Padding


## ECB mode

This is the simplest mode of encryption. ECB - Electronic Codebook. The padded message is divided into blocks and each block is encrypted separately using the block cipher algorithm (AES, DES, etc.). The encryption and decryption takes place as follows:

We know from Shannon's Theorem of perfect secrecy that the ciphertext should leave no hints about patterns existing in the plaintext. But ECB does leave some trace about patterns existing in the plaintext. Two blocks having the same data will give the same ciphertext blocks. By this the attacker can easily know that there are two blocks of plaintext which have the same data and thus it is not safe for use. This happens because the encryption of previous plaintext block does not affect the encryption of plaintext block next to it.

Here are two images, the second is an encrypted image of the first image, and as we can see, the patterns existing in the ciphertext which makes ECB mode unsafe for use 


## References
1. [Wikipedia- Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)