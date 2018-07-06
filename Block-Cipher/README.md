# Block Cipher
Block Cipher is a method of encrypting text using an algorithm which takes in a `key` (`iv` in some modes, as you will see), one block of data at a time, unlike stream ciphers which encrypt one byte of text at a time. Identical bytes of plaintext don't get encrypted into identical bytes of ciphertext in the case of block ciphers. Also, we must remember that even if one byte in a block of plaintext is changed/flipped, then the entire corresponding block of ciphertext changes in case of block cipher encryption. `Key` and `iv` are pseudo-random generated strings and their size depends upon the encryption algorithm being used. The block-size too, depends on the encryption algorithm being used (For example, block size for AES is fixed and equal to 16 bytes).  
  
  
## Padding
A block cipher works on a fixed size of data at a time known as the blocksize, but messages will not necessarily be a multiple of blocksize. In such cases, we need to add a fixed minimum number of bytes to the plaintext to make it a multiple of blocksize. The simplest way is to add null bytes to the plaintext to make it a multiple of blocksize. The other way is to add single 1 bit followed by zeros in the binary representation of the plaintext string. There are different standards for padding the plaintext.  
  
We must note that even if the plaintext size is a multiple of blocksize, the padding algorithm will still pad it with string of size equal to the blocksize. Why do you think this happens? Simple, to maintain text consistency. Padding needs to be removed after a ciphertext is decrypted, only then can the function return it. If there is no padding for plaintext having length a multiple of blocksize, then the function cannot identify if the last byte of a decrypted plaintext is a part of the padded string, or it is part of the plaintext, leading to consistency issues. And hence we always pad before encryption!  
A quick question, what is the minimum and maximum number of bytes that can be added to a plaintext to make it a multiple of blocksize? minimum=1, maximum=`blocksize` due to reasons we discussed above!  
  
  
## Mode of encryption
Read about it in detail [here](https://github.com/ashutosh1206/Crypto-Attacks/tree/master/Block-Cipher/Mode-of-Encryption)
  
  
## Block size detection
This section deals with the detection of blocksize in a block cipher. Suppose a program is running on a server we can `nc` to. The server takes in input from the user, pads it to make it a multiple of blocksize, encrypts it using a block cipher encryption algorithm and gives the ciphertext as the output to the user. Using this, we need to get the size of the block being used in the encryption algorithm. Suppose we send plaintext of size 1 byte and we get a ciphertext of size `x`. We then plaintext of size 2 bytes and check if the length of ciphertext is same as the length of previous ciphertext returned that is `x` here. We can keep increasing our input by 1 byte and checking if the length of ciphertext returned is equal to the length of the ciphertext previously returned. In case lengths do not match, then the blocksize is simply equal to the difference between the lengths of the two ciphertexts(the present and the previous one).  
  
Why does this happen? Remember from the padding section that when plaintext length becomes a multiple of blocksize, then the padding algorithm adds an entire block to the plaintext due reasons already discussed in _Padding_ section. So, we keep adding one byte to our input and noting the ciphertext length for each of our inputs. As soon as our input becomes a multiple of blocksize, an entire new block is added and hence the length of ciphertext changes. We can then compute blocksize = difference between the lengths of two ciphertexts(present and previous). Read about it in detail on my blog [here](https://masterpessimistaa.wordpress.com/2017/04/07/block-size-detection/)
  
  
## Mode Detection
This section will enable us to determine if the encryption of each block is dependent on the encryption of block next to it or not. Determining this is fairly easy, recall that in the case when the encryption of each block is independent, then two blocks having same data will have same data in their respective ciphertext blocks. So, for doing this, first we need to know the blocksize being used for encryption, which we can determine by the method discussed in _Block size detection_. Then, we can send two blocks of plaintext having same data and check if their corresponding ciphertext blocks match, if yes, then the mode of encryption is definitely ECB mode, otherwise the mode won't be ECB. Read about it in detail on my blog [here](https://masterpessimistaa.wordpress.com/2017/04/02/aes-mode-detection-oracle/)




