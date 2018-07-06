# CTR Bit Flipping Attack

Prerequisites:
1. [CTR mode of encryption](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Mode-of-Encryption)
2. [Block size detection](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/README.md)

Consider a scenario where there is a program running on a server. The server takes input from the user and does the following operations:
1. Checks if a particular character/substring is present in the input string, if yes then flips/changes them with appropriate characters
2. Prepends a string to the input
3. Appends another string to the resultant input string
4. Encrypts it using a block-cipher encryption in CTR mode
5. Returns the corresponding ciphertext as the output of the program
  

So consider registering under a name similar to encrypting the plaintext and logging in using the ciphertext cookie with the username as the same as the plaintext. As an attacker, we would like to exploit this and login as `admin` to get special privileges. But remember that the server flips some characters before generating the cookie(ciphertext) to disallow login in as admin. Here lies the application of CTR Bit Flipping Attack. The attack is similar to `CBC Bit Flipping Attack` with minute differences.
  
  
## Exploit

Suppose we want to login as "admin=true" but the server flips `=` to `?` before generating the cookie, so we would be able to login only as "admin?true" (Remember that we can login using the cookie, which is the ciphertext, and the server has generated ciphertext for `admin?true` and not `admin=true`). We need our username to be "admin=true" to get admin privileges. I would suggest you read the blog for CBC Bit Flipping attack [here](https://masterpessimistaa.wordpress.com/2017/05/03/cbc-bit-flipping-attack/) before moving onto Bit Flipping Attack for CTR mode. This attack for CTR is easier than one in CBC. If we closely look at decryption function in CTR mode below:

![decryption](https://upload.wikimedia.org/wikipedia/commons/3/3c/CTR_decryption_2.svg)

We can easily notice that the ciphertext of the respective block is xored with decryption of `nonce+counter` to give plaintext of the respective block. This can be written for each block as (C is the ciphertext block, P is the plaintext block and D() is the decryption oracle:
```
    C = D(nonce + counter) xor P
    For the nth byte of the block we can write:
    C[n] = D(nonce + counter)[n] xor P[n]
    D(nonce + counter)[n] = C[n] xor P[n]    ----> This is constant even if we flip/change some characters of C, look at the decryption oracle again
    D(nonce + counter)[n] = C[n] xor PF[n]   ----> PF because we want it to be a fixed plaintext block (reason above) 
    Therefore we can write,
    C[n] = C[n] xor PF[n] xor PD[n]    ----> PD is the value of plaintext desired
```
So the whole idea behind the attack is to locate the ciphertext index at which the flipped byte will be present, and xor the result with PD xor PF, where PD is the value of plaintext desired at that index and PF is the value of the plaintext that is already present in it. If we consider our example, then 
`C[n] = C[n] xor '?' xor '='` 
  
Now, if we send the resultant ciphertext to the decryption oracle/ login server, we will be able to login as "admin=true"!  
Check out example challenges based on this attack in the [Challenges](Challenges/) section.  




