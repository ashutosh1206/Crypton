# Authenticated Encryption

Authenticated Encryption is a technique used to combine encryption algorithms and MACs to generate a system that provides data security as well as authentication. There are two main methods by which this is established:
1. _Authenticated Encryption using MACs_: A combination of MACs and ciphers joined explicitly for achieving security and authenticity. Different types of AEuM:
   + Encrypt and MAC
   + MAC then Encrypt
   + Encrypt then MAC
2. _Authenticated Ciphers_: Systems designed specifically for authenticated encryption. They return a tag along with the ciphertext
  
  

## Authenticated Encryption using MACs
In this technique of implementing authenticated encryption, MACs are separately built along with an encryption system. There are various methods in which this can be done-
1. In one method ciphertext and authentication tag are produced parallely from a plaintext (Encrypt-and-MAC). 
2. In second method, authentication tag is generated from a plaintext, the result is concatenated with respective plaintext string and then encrypted (MAC-then-Encrypt). 
3. Third method involved encrypting the plaintext and generating the authentication tag from the resultant ciphertext string (Encrypt-then-MAC).
  

All these methods are discussed and implemented separately in different sections. You can look at them here:
1. [Encrypt and MAC](AE-with-MACs/Encrypt-and-MAC/)
2. [MAC then Encrypt](AE-with-MACs/MAC-then-Encrypt)
3. [Encrypt then MAC](AE-with-MACs/Encrypt-then-MAC/)
  

We have also covered drawbacks of using each technique (Security Analysis) and also the protocols where a technique finds it's applications.
  
  

## Authenticated Ciphers
Authenticated ciphers are encryption algorithms designed as one single entity to provide encryption and authentication. We can consider them as a standard established by combining a secure cipher and a strong MAC into one function that, on giving plaintext as input, returns corresponding ciphertext and it's authentication tag.  
  
Encryption can be denoted as **AE(k, P) = (C, T)**, where AE() is the cipher that takes in a key `k` and plaintext `P` as the input and returns ciphertext `C` and authentication tag `T`.  
  
Authenticated decryption takes place as follows: the algorithm takes ciphertext, authentication tag and key as input and returns corresponding plaintext only if the authentication process passes. Otherwise it simply returns `VerificationError`.  
  
This can be respresented as **AD(C, T, k) = P**, where AD() is authenticated decryption function.  
  
  
Security of Authenticated Cipher is affected by various factors:
1. Strength of authentication: Should be strong enough (as strong as the strongest MAC). This also implies that the authentication tag should not reveal anything about the plaintext whatsoever.
2. Safe, secure encryption algorithm
3. Inability to forge ciphertext and authentication tag without knowledge of the key
4. Predictability of the system
  
  

## Authenticated Encryption with Associated Data (AEAD)
There are situations where a standard/protocol demands encryption of a major part of the plaintext (not the entire plaintext), but authentication of the entire plaintext string.  
  
This usually happens when the receiver is required to read the header of a file received to recognise/verify certain standards of the protocol used for communication. If the entire plaintext string would have been encrypted, then the receiver would have to decrypt the ciphertext and then verify.  
  
So in order to make the process of secure communication more efficient and convenient, the concept of Authenticated Encryption with Associated Data (AEAD) came into picture.
  
In this way, even if the header/unencrypted text gets corrupted, the authentication will fail. Part of the plaintext, that is not encrypted but authenticated, is known as **Associated Data**   
  
Encryption in AEAD takes 3 parameters as input: plaintext, associated data and key and gives ciphertext and authentication tag as the output. We can respresent this as:  
**AEAD(P, A, k) = (C, T)**  
  
  
Similarly, decryption takes 4 parameters as input: ciphertext, associated data, key and authentication tag and gives plaintext, associated data as the output. This can be represented as:  
**ADAD(C, A, k, T) = (P, T)**  
  
  