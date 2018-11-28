# ElGamal Encryption

Prerequisites:
1. Cyclic Groups, Generators
2. Basic Number Theory (Euler's Theorem, Fermat's Little Theorem)


ElGamal Encryption System is an Asymmetric Key Encryption System based on [Discrete Logarithm Problem](../Discrete-Logarithm-Problem/) (DLP) and Diffie-Hellman Key Exchange.   

For illustrative purposes, we will consider `Alice` as the receiver and `Bob` as the sender.  

There are different steps involved while encrypting or decrypting data with ElGamal, let's list them first and then study each of them in detail:  
1. **Key Generation**:  Alice generates a public and private key and shares the public key.
2. **Encryption**: Bob uses Alice's public to encrypt message that he wants to send to Alice, and hence generates a pair of ciphertext (c1, c2). Shares the ciphertext pair.  
3. **Decryption**: Alice then uses her private key to decrypt the ciphertext (c1, c2).



## Key Generation
This is the first step in the process of transferring a messages securely, between Alice and Bob. In this step, Alice does the following:
1. Selects a Cyclic Group `G` of order `q` and generator `g`. Note that either the cyclic group should be generated over a [safe prime](https://en.wikipedia.org/wiki/Safe_prime) `p`, or the generator `g` should generate prime-order-subgroups; otherwise it is vulnerable to [Small Subgroup Attacks](https://florianjw.de/en/insecure_generators.html).
2. Generates a random number `x` such that `1 <= x <= q-1` and assigns it as the private key (Note that `q` is the group order).
3. Calculates ![picture1](Pictures/picture1.gif)
4. Shares `h`, `g`, `q` as Public Key
5. `x` is the Private Key which only Alice should know, and that's where the security of the encryption system lies.


Here is a python-2.7 implementation of the above step:  
```python
def _generate_key():
    	# Assigning the largest 1024-bit safe prime as p
	p = (1 << 1024) - 1093337
	x = randint(2, p-2)
	g = 23
	q = p - 1
	h = pow(g, x, p)
	pubkey = PublicKey(h, p, g, q)
	privkey = PrivateKey(x, p, g, q)
	return (pubkey, privkey)
```


## Encryption
Bob receives Alice's Public Key and encrypts the message that he wants to send to Alice as follows:  
1. Selects a random number `y` such that `1 <= y <= q-1`. Note that a new value of `y` is chosen for sending every message. Hence, `y` is known as ephemeral key.
2. Chooses a message `m` such that `1 < m < q-1`
2. Diffie Hellman Step: Calculates ![picture2](Pictures/picture2.gif)
3. Diffie Hellman Step, also `s` is known as the shared secret: Calculates ![picture3](Pictures/picture3.gif)
4. Calculates ![picture4](Pictures/picture4.gif)
5. Shares (c<sub>1</sub>, c<sub>2</sub>) as the ciphertext


Here is a python-2.7 implementation of the above step:  
```python
def _encrypt(message, pubkey):
  	h = pubkey.h
	p = pubkey.p
	g = pubkey.g
	q = pubkey.q
	m = bytes_to_long(message)
	# Generating ephemeral key: `y`
	y = randint(2, p-2)
	c1 = pow(g, y, p)
	# Computing the shared secret: `s`
	s = pow(h, y, p)
	c2 = (m*s) % p
	return (c1, c2)

```


## Decryption
Alice receives (c<sub>1</sub>, c<sub>2</sub>), we can write them as:  
![picture](Pictures/picture2.gif)  
![picture](Pictures/picture4.gif)  
1. Alice then calculates the following to get the shared secret `s`: ![picture7](Pictures/picture5.gif)
2. To get back the message `m` from c<sub>2</sub>, Alice does the following:  
![picture8](Pictures/picture6.gif)  


Here is a python-2.7 implementation of the above step:  
```python
def _decrypt(ciphertext, privkey):
	c1, c2 = ciphertext
	g = privkey.g
	p = privkey.p
	x = privkey.x
	s = pow(c1, x, p)
	m = (c2*inverse(s, p)) % p
	return m
```

Check out the full implementation/example of ElGamal encryption/decryption [here](example.py)

## References
1. [Wikipedia- ElGamal Encryption](https://en.wikipedia.org/wiki/ElGamal_encryption)
2. [Small Subgroup Attacks- Florianjw's blog](https://florianjw.de/en/insecure_generators.html)
