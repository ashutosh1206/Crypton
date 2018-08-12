# Franklin Reiter's Attack on related messages

Prerequisites:
1. [RSA Encryption/Decryption](https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/README.md) 
2. [Coppersmith's Theorem](https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-Coppersmith/README.md)

This attack works in a scenario where two messages differ only by a fixed known difference and are encrypted using public key e and same modulus N. The attacker can then recover the two messages in the above scenario using Franklin Reiter's Attack.

## Theorem
Suppose there are two messages M<sub>1</sub> and M<sub>2</sub> where M<sub>1</sub> != M<sub>2</sub>, both less than N and related to each other as ![equation](Pictures/1.gif) for some linear polynomial ![equation](Pictures/2.gif) where b!=0. These two messages are to be sent by encrypting using the public key (N, e), thus giving ciphertexts C<sub>1</sub> and C<sub>2</sub> respectively. Then, given (N, e, C<sub>1</sub>, C<sub>2</sub>, f), the attacker can recover messages M<sub>1</sub> and M<sub>2</sub>.
  
  
## Proof
We can write C<sub>1</sub> and C<sub>2</sub> as:  
![equation](Pictures/3.gif)  
We can also write,  
![equation](Pictures/4.gif)  
![equation](Pictures/5.gif)  
We can then write the polynomials g<sub>1</sub>(x) and g<sub>2</sub>(x) as:  
![equation](Pictures/6.gif)  
![equation](Pictures/7.gif)  
So clearly M<sub>2</sub> is a root of both the polynomials above and hence they have a common factor **x-M<sub>2</sub>** (Since, g<sub>1</sub>(M<sub>2</sub>) = 0 and g<sub>2</sub>(M<sub>2</sub>) = 0)
Therefore, we can simply calculate GCD of g<sub>1</sub> and  g<sub>2</sub> and if the resultant polynomial is linear, then we get out M<sub>2</sub> and hence M<sub>1</sub>!  
  
    Exploit in a nutshell:
    1. Calculate g1 and g2 as given above
    2. Calculate GCD(g1, g2) and check if the resultant polynomial is linear or not
    3. If the resultant polynomial is linear, then return GCD
  
Check the **implementation** of the above attack [here](exploit.sage)
  
## References
1. [Wikipedia- Franklin Reiter's related message attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#Franklin-Reiter_related-message_attack)

