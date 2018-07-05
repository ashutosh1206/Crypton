## Detecting IV in CBC mode

Prerequisites:
1. [CBC mode of encryption](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Mode-of-Encryption)
2. [Block Size detection](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/README.md)

This section will help us get the value of the **Initialisation Vector** (IV) in CBC mode when its value is not known. This exploit is particularly helpful in attacks such as [Padding Oracle Attack](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Padding-Oracle), which requires knowledge of IV to get the value of first block of plaintext.  
  
Consider a scenario where there is a program running on a server which encrypts/decrypts data given to it as an input. The encryption/decryption is based on a block cipher in CBC mode. We only have access to input and output and we need to know the value of IV using this.  
  
Suppose we send an input of size > 32 bytes. Then after padding the minimum size of our plaintext input will be 48 bytes. We want this as a minimum due to reasons which you will come to know later. As of now, consider the conditions. We will get a ciphertext as an output, let it be assigned as `ciphertext`. For our attack, we will select first three blocks of ciphertext because IV is directly used in the first block.  

![decryption](https://upload.wikimedia.org/wikipedia/commons/2/2a/CBC_decryption.svg)

We will write down equations for each plaintext block: (First block of plaintext as p1, second as p2 and so on)
```
    p1 = D(c1) xor iv
    p2 = D(c2) xor c1
    p3 = D(c3) xor c2
```

When c1 = c3 and c2 is an empty block, i.e. c2 = "\x00"*blocksize, then 
```
    p1' = D(c1) xor iv
    p2' = D("\x00"*blocksize) xor c1
    p3' = D(c3 = c1) xor "\x00"*blocksize = D(c1)
```
We can now simply calculate iv as `p1' xor p3'`. So we call the decryption oracle and give the ciphertext input as `c1 + "\x00"*blocksize + c1`. We can now XOR the first block of plaintext output and the third block of plaintext output to get IV.  
  
I have written a script in python to illustrate working of the above exploit. You can check it here- [example.py](example.py).





