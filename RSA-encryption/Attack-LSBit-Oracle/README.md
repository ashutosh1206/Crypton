# Least Significant Bit Oracle Attack

Prerequisites:
1. [RSA Encryption/Decryption](../../RSA-encryption/README.md)

This attacks works due to leaking of the Least Significant Bit by an unpadded RSA encryption/decryption oracle. It enables the adversary to get the plaintext from the ciphertext in ![picture](Pictures/1,gif) requests to the oracle. In this article we will try to understand the logic and details behind LSB oracle attack on unpadded RSA.
