# Hastad's Broadcast Attack

Prerequisites:
1. [RSA Encryption/Decryption](https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/README.md)
2. [Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)

We will start by discussing the simplest form of Hastad's Broadcast Attack and then generalise the attack using Coppersmith's Theorem.

## Hastad's Broadcast Attack on unpadded message
Suppose Alice sends an unpadded message M to `k` people P<sub>1</sub>, P<sub>2</sub>, ..., P<sub>k</sub> each using a same small public key exponent `e` and different moduli `N` for ith individual, the public key for ith individual (N<sub>i</sub>, e). The attack states that as soon as `k>=e`, the message M is no longer secure and we can recover it easily using Chinese Remainder Theorem. Let us see how, using an example: Alice sends a message M to 3 three different people using the above conditions and using the same public key exponent `e = 3`. Let the ciphertext received by ith receiver be C<sub>i</sub> where C<sub>i</sub> = M<sup>3</sup> mod N<sub>i</sub>. We have to assume that **gcd(N<sub>i</sub>, N<sub>j</sub>)** where `i != j` (Otherwise if we get a common factor between a pair of moduli let us suppose it to be k, we can factorise both of them, since we then know one of the factors of N<sub>i</sub> and we can calculate the other as N<sub>i</sub>/k). We can now write:

![equation](https://latex.codecogs.com/png.latex?{\displaystyle&space;M^{3}\equiv&space;C_{1}{\pmod&space;{N_{1}}}})  
![equation](https://latex.codecogs.com/png.latex?{\displaystyle&space;M^{3}\equiv&space;C_{2}{\pmod&space;{N_{2}}}})  
![equation](https://latex.codecogs.com/png.latex?{\displaystyle&space;M^{3}\equiv&space;C_{3}{\pmod&space;{N_{3}}}})  

Thus we can get the following by solving using Chinese Remainder Theorem:
![equation](https://latex.codecogs.com/png.latex?M^{3}&space;=&space;\sum_{i=1}^3&space;C_i&space;b_i&space;b'_i&space;\pmod{N})
where **b<sub>i</sub> = N/N<sub>i</sub>** , **b<sub>i</sub><sup>'</sup> = b<sub>i</sub><sup>-1</sup> mod N<sub>i</sub>** and N = N<sub>1</sub>*N<sub>2</sub>*N<sub>3</sub>. Since we know that M < N<sub>i</sub> (If our message M is larger than the modulus N, then we won't get the exact message when we decrypt the ciphertext, we will get an equivalent message instead, which is not favourable). Therefore we can write M < N<sub>1</sub>N<sub>2</sub>N<sub>3</sub>. We can easily calculate M now by directly taking the `cube root` of M<sup>3</sup> to get `M`.


## Hastad's Broadcast Attack on padded message
Hastad also showed that applying `linear padding` to the message M prior to encryption does not protect from this attack. Assuming C<sub>i</sub> = f<sub>i</sub>(M)<sup>e</sup> for 1<=i<=k (k --> number of individuals the message is to be sent/has been sent). Here f<sub>i</sub> is a linear function to pad the message M, so that the recipients receive slightly different messages. For ith individual, Message M = i*2<sup>m</sup> + M, where m is the number of bits in M. Hastad proved that a system of univariate equations modulo relatively prime composites, such as applying fixed polynomial ![equation](https://latex.codecogs.com/png.latex?{\displaystyle&space;g_{i}(M)\equiv&space;0{\pmod&space;{N_{i}}}}) could be solved if sufficient equations are provided. This attack is an application of Chinese Remainder Theorem and Coppersmith's Theorem.  
![proof](https://i.imgur.com/ivFhUEj.png)

    Exploit in a Nutshell:
    1. Calculate N = n1*n2*... 
    2. Calculate each element T[j] as per the above conditions using CRT
    3. Assign P.<x> = PolynomialRing(Zmod(N))
    4. g[j] = (i*(2^m) + x)^e - c, where the message is padded using the above conditions
    5. Assign g = Sum_of(T[j] * g[j])
    6. Check if g is a monic polynomial, if not transform it into a monic polynomial
    7. Find small roots of g and check if that is the flag



## Resources
1. [Wikipedia- Coppersmith's Attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack)
2. [Wikipedia- Chinese Remainder Theorem](https://en.wikipedia.org/wiki/Chinese_remainder_theorem)
3. [Cryptanalysis of RSA using Lattice Methods](http://theory.stanford.edu/~gdurf/durfee-thesis-phd.pdf)


