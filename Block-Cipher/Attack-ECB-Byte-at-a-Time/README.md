# ECB Byte at a Time Attack

Before getting acquainted with the attack, one must know the following:
1. ECB mode of encryption
2. Block Size detection
3. Block Cipher mode detection

This attack is one of the simplest and easy to understand attacks existing in block ciphers. We must understand that each attack works under a specific scenario and this attack too work under certain conditions. Consider the following scenario: 
1. There is a block cipher encryption code running in a server
2. The server takes input from the user
3. Appends a secret string to the input
4. Pads it to make it a multiple of blocksize
5. Encrypts it using a block cipher encryption algorithm
6. Gives the ciphertext as the output

In the beginning, as an attacker we have no idea about:
1. Block size of encryption system
2. Block cipher mode of encryption

So, our first task is to know about all of them, which we have already discussed in other topics under `Block Cipher`.
Let us now consider that using the previous articles written, we now know about the block size and the block cipher mode of encryption. The attacker's motive is to get the value of the secret. Suppose we send an input to the server of size equal to the blocksize of the cipher, let us analyse the block division of the string being encrypted: 
```
        1st Block | 2nd Block | 3rd Block | ...
        Input     | Secret    | secret+padding ...
```

When we send an input of size one less than the blocksize of the cipher, let us again analyse the block division of the string being encrypted:
```
        1st Block | 2nd Block, 3rd Block ...
        x         | Secret[1:]+padding ...
```

Here `x = input + Secret[0]` and let the output in this case be `c1`. The first block now contains (blocksize - 1) bytes of input and 1 byte of secret. Since in ECB mode, encryption of one block is independent of the other, we can brute-force 256 possibilities for the last byte of first block, by sending the input as the same (blocksize - 1)bytes and 1 brute-force byte to the server and noting the ciphertext for each iteration, let that be `c2`. For each iteration, note the brute-force byte when the first block of `c1` matches with the first block of `c2`. In this way, we get the first byte of secret.

Next, we send input equal to 2 bytes less than the blocksize plus one byte of the secret we previously got and brute-force again. 
We keep bruteforcing each byte until we get all the bytes of the secret. 

