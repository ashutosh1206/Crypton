# Coppersmith's Theorem and Attack

Prerequisites: 
1. RSA Encryption/Decryption
2. Univariate Monic Polynomial


## Coppersmith's Theorem
Let a monic polynomial ![equation](https://latex.codecogs.com/gif.latex?{\displaystyle&space;f\in&space;{\mathbb&space;{Z}&space;}[x]}) of degree `d` with integer coefficients and integers `X` and `N` be given. Suppose ![equation](https://latex.codecogs.com/png.latex?X=N^{{{\frac&space;{1}{d}}-\epsilon&space;}}) for some ![equation](https://latex.codecogs.com/png.latex?\epsilon&space;>0). There is an algorithm to find all ![equation](https://latex.codecogs.com/gif.latex?x_{0}<X) satisfying ![equation](https://latex.codecogs.com/gif.latex?{\displaystyle&space;f(x_{0})\equiv&space;0{\pmod&space;{N}}}&space). The algorithm runs in time <strong>O(T<sub>LLL</sub>(m*d, m*logN))</strong> where `m = O(k/d)` for `k=min{1/epsilon, logN}`
## Coppersmith's Attack
To understand this attack watch this video by David Wong on `Attacking RSA with Lattice Reduction Techniques`. The explanation is clear, precise and enough to understand the listed attacks. Link to the video: [Attacking RSA with Lattice Reduction Techniques: David Wong](https://www.youtube.com/watch?v=3cicTG3zeVQ). Assumming that you have watched the video now, we can now move on to discuss application of Coppersmith's Theorem in relaxed models/scenarios. [This](https://link.springer.com/chapter/10.1007/BFb0024458) paper by Howgrave-Graham suggests that we can convert the polynomial `f(x)` into another polynomial `g(x)` having the same roots but smaller coefficients and in the same vector space. This can be done efficiently by Lattice Reduction Techniques as explained in the video too. There are different scenarios where Coppersmith's Theorem can be applied.
1. Scenario #1- Stereotyped Messages
2. Scenario #2- Factoring `N` with high bits known 
3. Scenario #3- Boneh-Durfee Attack (Described separately)


## Stereotyped Messages
In this scenario, we know the most the significant bits of the message. Applying the above theorem, we can find the rest of the message. This happens in cases where the message is something like: "The secret is: XXXXXXXX". We don't know 'XXXXXXXX' and by Coppersmith's Theorem we can find it. Now the question that arises is: How? Coppersmith says that if we are looking for <strong>N<sup>1/e</sup></strong> of the message, it is then a `small root` and we will be able to find it quickly. Let us formulate our `f(x)` in such situations:
`f(x) = (m + x)**e - c`. Here m is the message which is known to us, `c` is the corresponding ciphertext of the entire message, `e` is the public key exponent and `x` is a `Polynomial Ring of integers over modulo N`. We can now write:
```
    P.<x> = PolynomialRing(Zmod(N))
    beta = 1
    dd = f.degree()    # Degree of the polynomial
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    f.small_roots(XX, beta, epsilon)
```
Check if each root is printable and matches with the message. You can check out the python/sage **implementation** of the above scenario [here](exploit.py)


## Factoring `N` with high bits known
In this scenario we know the most significant bits of one of the factors of the modulus `N`. Suppose we know an approximation of q: `q'`, we can then write f(x) as `q' - x`. 
```
    P.<x> = PolynomialRing(Zmod(N))
    beta = 0.5
    dd = f.degree()    # Degree of the polynomial
    epsilon = beta/7
    XX = ceil(N**((beta**2/dd) - epsilon))
    f.small_roots(XX, beta, epsilon)
```
You can check the python/sage **implementation** of the above scenario [here](exploit.py)





## References
1. [Finding small solutions to small degree polynomials- Don Coppersmith](https://cr.yp.to/bib/2001/coppersmith.pdf)
2. [Finding small roots of univariate modular equations- Howgrave-Graham](https://link.springer.com/chapter/10.1007/BFb0024458)
3. [Wikipedia- Coppersmith's Method](https://en.wikipedia.org/wiki/Coppersmith_method)
4. [Wikipedia- Coppersmith's Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)
