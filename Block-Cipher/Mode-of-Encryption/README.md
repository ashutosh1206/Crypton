# Mode of encryption
A block cipher takes in a block of data of size equal to the blocksize, a key (and an IV in some cases). The algorithm does not know of how encryption of each block of data affects the blocks present next to it. This is in fact governed by the mode in which the data is encrypted in a block cipher.

Prerequisite:
1. Block Cipher
2. Padding


## ECB mode (Electronic CodeBook)

This is the simplest mode of encryption. The padded message is divided into blocks and each block is encrypted separately using the block cipher algorithm (AES, DES, etc.). The encryption and decryption takes place as follows:

![picture1](https://upload.wikimedia.org/wikipedia/commons/d/d6/ECB_encryption.svg)

![picture2](https://upload.wikimedia.org/wikipedia/commons/e/e6/ECB_decryption.svg)


We know from Shannon's Theorem of perfect secrecy that the ciphertext should leave no hints about patterns existing in the plaintext. But ECB does leave some trace about patterns existing in the plaintext. Two blocks having the same data will give the same ciphertext blocks. By this the attacker can easily know that there are two blocks of plaintext which have the same data and thus it is not safe for use. This happens because the encryption of previous plaintext block does not affect the encryption of plaintext block next to it.

Here are two images, the second is an encrypted image of the first image, and as we can see, the patterns existing in the ciphertext which makes ECB mode unsafe for use:

![plainimage](https://upload.wikimedia.org/wikipedia/commons/5/56/Tux.jpg)
![cipherimage](https://upload.wikimedia.org/wikipedia/commons/f/f0/Tux_ecb.jpg)


## CBC mode (Cipher Block Chaining)

This mode is one of the most commonly used mode of encryption. In this mode of encryption, the plaintext is XORed with the ciphertext of the previous block before giving as an input to the block cipher. For the first block, plaintext is XORed with an IV (Initialisation Vector) which can be assigned a value as per choice. The encryption takes place as follows (Assuming the first block has index 1): C<sub>i</sub>: E<sub>k</sub>(P<sub>i</sub> xor C<sub>i-1</sub>),  C<sub>0</sub> = IV. The decryption takes place as follows (Assuming the first block has index 1): P<sub>i</sub> = D(C<sub>i</sub>) xor C<sub>i-1</sub>. This is the picturised representation of encryption-decryption algorithms:

![encryption](https://upload.wikimedia.org/wikipedia/commons/8/80/CBC_encryption.svg)
![decryption](https://upload.wikimedia.org/wikipedia/commons/2/2a/CBC_decryption.svg)


## CTR mode (Counter Mode)

This mode of encryption converts a block cipher into a stream cipher. Picturised representation of CTR mode of encryption/decryption:

![encryption](https://upload.wikimedia.org/wikipedia/commons/4/4d/CTR_encryption_2.svg)
![decryption](https://upload.wikimedia.org/wikipedia/commons/3/3c/CTR_decryption_2.svg)

As the picture suggests, a stream of bytes is encrypted using the block cipher encryption algorithm instead of the plaintext bytes being encrypted. The encrypted stream of bytes are then XORed with the plaintext to give the corresponding ciphertext. A point to be noted here is that the stream of bytes for each block should be unique or otherwise it would lead to some serious security issues. That is why we use a counter inside the stream of bytes being encrypted along with a unique string called the `nonce`. The nonce remains the same for each block, but the counter value increases by 1 for each block. Note that in this mode, there is no need of decryption oracle as the stream of bytes are always being encrypted using the block cipher and then xored. We just have to XOR it with ciphertext/plaintext depending on whether we are going to decrypt/encrypt respectively. 



## References
1. [Wikipedia- Block cipher mode of operation](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation)
