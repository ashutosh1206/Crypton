# Forbidden Attack on AES-GCM

Prerequisites:
1. Finite Fields
2. [AES-GCM](../)
  
  

In this section, we will discuss an attack on AES-GCM due to reusage of nonce during encryption process. The attack can reveal value of `H` which can then help the attacker to forge authentication tag `T`.  
  
We will be using the same symbols as we did while discussing the internals of [AES-GCM](../)  
  

## Deriving Polynomial for Authentication Tag
In this section, we will see polynomial representation of authentication tag generation.  
  
We know that the tag is generated using a series of multiplication over finite field GF(2<sup>256</sup>) and GF(2**256) is an Extension Field.
  
There are broadly two categories of Finite Fields: Prime Fields and Extension Fields. Prime Fields are of the form GF(p) where `p` is a prime number and consist of integers in {0,..., p}. Extension fields are of the form GF(p<sup>m</sup>), where `p` is a prime number and `m` is a positive integer and consist of polynomials of the form
> a<sub>m-1</sub>x<sup>m-1</sup> + a<sub>m-2</sub>x<sup>m-2</sup> + ... + a<sub>1</sub>x + a<sub>0</sub>  
  

Here, `a` can assume values in {0,..., p-1}  
  

GF(2<sup>m</sup>) is one of the most frequently used fields in cryptography. Since multiplication in AES-GCM happens over Finite Field GF(2<sup>256</sup>) (Extension Field), elements of this Finite Field are polynomials.  
  
Hence, all the computation discussed in [authtag generation process of AES-GCM](https://github.com/ashutosh1206/Crypton/tree/master/Authenticated-Encryption/AES-GCM#authentication-tag-generation-in-aes-gcm) is over polynomials (The function `mod_polynomial_mult(self, a, b, p)` in authtag process is an implementation of multiplication of two polynomials `a` and `b` modulo an irreducible polynomial  `f = 1 + x + x<sup>2</sup> + x<sup>7</sup> + x<sup>128</sup>` over GF(2<sup>256</sup>)).  
  
  
We will discuss a trivial case scenario in encryption and authtag generation part of AES-GCM, and then derive the generalised polynomial that can be used to generate authentication tag.  
  
**Note**: Polynomial Addition over a Finite Field GF(2<sup>m</sup>) is equivalent to XOR operation over integers.
  
  

**Case Scenario-1**: Alice (sender) wants to use AES-GCM to encrypt _one_ block of plaintext (16 bytes) and generate authentication tag for _one_ block of associated data and _one_ block of ciphertext corresponding to the _one_ block of plaintext.  
  
Authentication Tag in this case can be written as:  
> g(X) = ((A<sub>1</sub>X + C<sub>1</sub>)X + L)X + S  

where L is len(A) || len(C), S is E<sub>k</sub>(J<sub>0</sub>) and X is the authentication key. The above polynomial is equal to:  
> g(X) = A<sub>1</sub>X<sup>3</sup> + C<sub>1</sub>X<sup>2</sup> + LX + S
  
  

**Case Scenario-2**: Alice (sender) wants to use AES-GCM to encrypt _two_ blocks of plaintext (32 bytes) and generate authentication tag for _two_ blocks of associated data and _two_ blocks of ciphertext corresponding to _two_ blocks of plaintext.  
  
Authentication Tag in this case can be written as:  
> ((((A<sub>1</sub>X + A<sub>2</sub>)X + C<sub>1</sub>)X + C<sub>2</sub>)X + L)X + S  

This is equal to:  
> A<sub>1</sub>X<sup>5</sup> + A<sub>2</sub>X<sup>4</sup> + C<sub>1</sub>X<sup>3</sup> + C<sub>2</sub>X<sup>2</sup> + LX + S
  
  

**Generalised polynomial**: We can now define polynomial for generation of authentication tag with `m` blocks of associated data and `n` blocks of plaintext:  
> g(X) = A<sub>1</sub>X<sup>m+n+1</sup> + ... + A<sub>m</sub>X<sup>n+2</sup> + C<sub>1</sub>X<sup>n+1</sup> + ... + C<sub>n</sub>X<sup>2</sup> + LX + S  

where L is len(A) || len(C), S is E<sub>k</sub>(J<sub>0</sub>) and X is the authentication key. Also, when X=H, **g(H) = T** (T is the authentication tag generated in AES-GCM)  
  

Now that we have derived polynomial expression for authentication tag generation in AES-GCM, let us see how the Forbidden Attack works!
  
  

## The Forbidden Attack
For simplicity of understanding, consider a scenario where Alice (sender) sends two messages containing _one_ block of plaintext (16 bytes) each (no associated data blocks) and generates authentication tag for ciphertext of each message using the same nonce. Our intention, as an attacker is to find out the value of `H` that is the authentication key.  
  
**Note**: An important condition for this attack to work is for nonce to be reused in generating ciphertext and authentication tag pair of two different messages.  
  
We denote authentication tag polynomials for the two messages as g<sub>1</sub>(X) and g<sub>2</sub>(X). Each polynomial can be written as:  
> g<sub>1</sub>(X) = C<sub>1,1</sub>X<sup>2</sup> + L<sub>1</sub>X + S  
> g<sub>2</sub>(X) = C<sub>2,1</sub>X<sup>2</sup> + L<sub>2</sub>X + S  

where C<sub>1,1</sub> and C<sub>2,1</sub> signify first block of ciphertext corresponding to the first message and first block of ciphertext corresponding to the second message respectively.  
  
Note that `S` and `L` are same for both the polynomial expressions.  
We know that `L = len(A) || len(C)`, none of the messages have any associated data and both of them have same lengths of ciphertext = 16 bytes. Hence, `L` is same for both polynomial expressions.  
We also know that S = E<sub>k</sub>(J<sub>0</sub>) and J<sub>0</sub> contains Nonce. Since the two messages use same Nonce, we have same values of `S` for the above polynomial expressions.  
  
Also, we cannot solve any of the above polynomials separately and get the value of X. Why? Because we don't know the value of S = E<sub>k</sub>(J<sub>0</sub>). If by any method we can eliminate `S` from the expression, and equate the polynomial to zero, we can simply solve the quadratic equation and get the value of `X` (authentication key). Let us now see how we can do that.  
  
We know that g<sub>1</sub>(H) = T<sub>1</sub> and g<sub>2</sub>(H) = T<sub>2</sub>, adding T<sub>1</sub> on both sides of polynomial 1 and T<sub>2</sub> on both sides of polynomial 2, we can write:  
> g'<sub>1</sub>(X) = C<sub>1,1</sub>X<sup>2</sup> + L<sub>1</sub>X + S + T<sub>1</sub>  
> g'<sub>2</sub>(X) = C<sub>2,1</sub>X<sup>2</sup> + L<sub>2</sub>X + S + T<sub>2</sub>  
  
  

g'<sub>1</sub>(H) = g'<sub>2</sub>(H) = 0, (Since g(H) = T, g(H) + T over a Finite Field of the form GF(2<sup>m</sup>) will be equivalent to g(h) ^ T = 0). Now we add the two polynomials to get:  
  
> f(X) = (C<sub>1,1</sub>+C<sub>2,1</sub>)X<sup>2</sup> + (L<sub>1</sub> + L<sub>2</sub>)X + (T<sub>1</sub> + T<sub>2</sub>)  
  

We know that f(H) = 0, so we can easily solve the above quadratic equation to get all possible values of `H`. The number of possible values of `H` will be equal to the degree of the polynomial which, in turn, depends upon the number of plaintext and associated data blocks.  
  
After we get the value of `H` we can easily generate authentication tag for any message by calling the `authtag_gen()` function from [AES-GCM-implementation.py](../AES-GCM-implementation.py)!
  
  

## References
1. [Nonce Disrespecting Adverseries: Practical Forgery Attacks on GCM in TLS](https://eprint.iacr.org/2016/475.pdf)