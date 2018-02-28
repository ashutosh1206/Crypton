# CBC-MAC Forgery

Prerequisites:
1. [CBC mode of encryption](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Mode-of-Encryption)
  
  

## CBC-MAC
CBC-MAC is similar to CBC mode of encryption, just that instead of returning the entire ciphertext as in the case of CBC-encryption, CBC-MAC just returns the last block of ciphertext as the **authentication tag**.  
  
  
## CBC-MAC Vulnerability
**Attacker's motive**: Generate two different messages M1 and M2 having the same Authentication Tag T = MAC(k, M1) == MAC(k, M2), without having the knowledge of key k. This will enable the attacker to change the message being sent from M1 to M2 having same authentication tag. When Bob (receiver) gets the message, he won't come to know that the message has been changed, and will believe that the message he received came from Alice (sender) (Attacker now can pretend to be Alice since he has control over the message being sent to Bob)
  
Case Scenario:
1. Code running on a server which allows the user to generate Authentication Tag (or commonly known as MAC) by giving message as the input M
2. Internal Comptation: Server encrypts M using a block cipher algorithm in CBC mode to give ciphertext C
2. Returns last block of the ciphertext ie. C[len(C) - blocksize:] as the Authentication Tag
  

**The vulnerability**:  
![picture1](https://i.imgur.com/o4oUSwh.png)  
Vulnerability exists in the encryption of second block according to the above image. Let us discuss how:  
y = E(P1 xor IV) xor P2, where P1 is the first block of plaintext, P2 = x is the second block of plaintext, IV is the initialisation vector.  
Note that there can exist multiple pairs of P1 and P2 that will give the same value of y.  
Same values of y will result in same values of **Authentication Tag**   
  
  
## The Exploit  
1. Send an input string i1 of size < blocksize and save the MAC for this string --> MAC(i1)
2. Send an input string i2 of size < blocksize and save the MAC for this string as well --> MAC(i2)
3. Send an input string s1 of value = i1 + 'a'*15 + '\x01', MAC for this string = E(MAC(i1) xor ('a'*15 + '\x01')) --> MAC(i1) xor ('a'*15 + '\x01') is 'y' as per the above image 
4. We need a string i3 which when xored with MAC(i2) will give the same value as MAC(i1) xor ('a'*15 + '\x01'). We can then write i3 = MAC(i2) xor MAC(i1) xor ('a'*15 + '\x01')
5. Send an input string s2 of value = i2 + i3, MAC for this string will be E(MAC(i2) xor i3) = E(MAC(i2) xor MAC(i2) xor MAC(i1) xor ('a'*15 + '\x01')) = 'y' as per the above image
6. Now we have two strings s1 and s2 that are different but have the same Authentication Tag. Thus the attacker has successfully created a CBC-MAC Forgery.