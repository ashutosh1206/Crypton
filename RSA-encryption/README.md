# RSA - Public Key Cryptosystem

RSA is one of the first public key cryptosystem used commercially for secure data transmission. The key is asymmetric, meaning that the key used for encryption and the key used for decryption is not the same. As we go through how the encryption/decryption works, we will understand why the cryptosystem is called <strong>public key</strong> cryptosystem. Unlike symmetric key cryptosystems, there exists two pairs of keys in Public Key Cryptosystems: A private key pair and a public key pair. Each individual has his/her own set of unique private-public keys. The private key is completely secret for each individual and only he/she knows it's value, whereas public key of an individual who wants to receive a message is sent to anyone who wants to send a message, via a reliable channel. We will see what exactly reliable channel means, as we move through the explanation.

There are several steps in the process of encryption/decryption:
1. Key Generation
2. Key Distribution
3. Encryption/Decryption

We will also discuss attacks on RSA due to vulnerabilties in implementation and in the end discuss the need for `padding` in RSA.

Let us first define variables that will be repeatedly used:
1. p,q : Two very large primes 
2. n : Modulus, n = p*q
3. e : Public key exponent
4. d : Private key exponent
5. M : Unpadded message
3. m : Padded message
4. c : Ciphertext
5. ![equation](https://latex.codecogs.com/png.latex?{\varphi()}) : [Euler's totient Function](https://en.wikipedia.org/wiki/Euler%27s_totient_function)


## Key Generation
1. Choose two distinct primes <strong>p</strong> and <strong>q</strong>. Both the primes must be chosen randomly and must be similar in magnitude. There should be a significant difference in the values of the primes otherwise it will become vulnerable to <strong>Fermat's Factorisation</strong> and we will see how and why is it so.
2. Compute n = p*q
3. Calculate the value of ![equation](https://latex.codecogs.com/png.latex?{\varphi(n)}) = (p-1)*(q-1) in this case. 
4. Choose an integer `e` such that 1 < e < ![equation](https://latex.codecogs.com/png.latex?{\varphi(n)}) and gcd(e, ![equation](https://latex.codecogs.com/png.latex?{\varphi(n)})) = 1. `e` is often selected small and to be in the form of 2<sup>2<sup>i</sup></sup>+1 also known as [Fermat Numbers](https://en.wikipedia.org/wiki/Fermat_number), because it makes exponentiation more efficient. This makes it vulnerable to some attacks in some situations and we will see how we can prevent them.
5. Compute `d` as d = e<sup>-1</sup> mod ![equation](https://latex.codecogs.com/png.latex?{\varphi(n)})
6. The pair `(e, n)` is known as public key and `(d, n)` is known as private key.


## Key Distribution
Suppose Bob wants to send a message to Alice. If they decide to use RSA, Bob must know Alice's public key to encrypt the message and Alice must use her private key to decrypt the message. To enable Bob to send his encrypted messages, Alice transmits her public key (n, e) to Bob via a reliable, but not necessarily secret, route. Alice's private key (d) is never distributed. Reliable channel --> The keys are sent without any alterations in their values. 


## Encryption
After Bob receives Alice's public key, he does the following operations:
1. Pads the message M using an agreed-upon reversible padding scheme to get m
2. Computes ciphertext c = m<sup>e</sup> mod n
3. Transmits the ciphertext c using a reliable channel


## Decryption
After receiving the ciphertext c from Bob, Alice computes the following to get back the message:
1. Computes m = c<sup>d</sup> mod n (Since c = m<sup>e</sup> mod n, c</sup>d</sup> mod n = m<sup>e*d</sup> mod n = m. See proof under `Proof of decryption using Euler's Theorem`)
2. Reverse the padding scheme to get back M


### Proof of decryption using Euler's Theorem
Read about Euler's Theorem [here](https://en.wikipedia.org/wiki/Euler%27s_theorem)

c = M<sup>e</sup> mod n  
c<sup>d</sup> mod n = M<sup>ed</sup> mod n  
Since we have from Euler's theorem that: ![equation](https://latex.codecogs.com/png.latex?a^{\varphi&space;(n)}&space;\equiv&space;1&space;\pmod{n}), we can now write  
![equation](https://latex.codecogs.com/png.latex?{\displaystyle&space;m^{ed}=m^{1&plus;h\varphi&space;(n)}=m(m^{\varphi&space;(n)})^{h}\equiv&space;m(1)^{h}\equiv&space;m{\pmod&space;{n}}})



Read about RSA here: [Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))
