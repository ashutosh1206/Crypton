# Wiener's Attack

Prerequisites: 
1. RSA encryption/decryption
2. [Continued Fractions](https://en.wikipedia.org/wiki/Continued_fraction) --> Read only basic intro to get an idea of what are continued fractions and also about Infinite Continued Fractions to get a basic idea of convergents

Wiener's Attack is based on the vulnerability that when `d < N<sup>0.25</sup>`, then the one of the convergents of Continued Fraction of `e/N` is `k/d` where k satisfies this equation- ![equation](https://latex.codecogs.com/png.latex?ed-k\varphi&space;(N)=1). This equation is derived from- ![equation](https://latex.codecogs.com/png.latex?ed\equiv&space;1\:{\bmod\:\varphi}(N)). We will see what exactly does the above statement mean and also see its proof in this write-up. To understand the statement above, it is essential to understand what are continued fractions and the concept of convergents in infinite fractions. Considering the reader has read it using the link provided in the `Prerequisites` section, we will discuss why convergents are important by understanding how the attack works.


## Wiener's Theorem
Let `N = pq` with `q < p < 2q`. Let ![equation](https://latex.codecogs.com/png.latex?d<{\frac&space;{1}{3}}N^{{{\frac&space;{1}{4}}}}). Then given `(e, n)`, the attacker can efficiently recover `d`.


## Proof of Wiener's Theorem
![picture](https://i.imgur.com/ffMrM2g.png)
![picture](https://i.imgur.com/6XcUkKi.png)


## Attack
1. Store the convergents of continued fraction of e/n in a list
2. Iterate over each element in the list
3. For each iteration assign the denominator of the convergent as `d`
4. Decrypt the ciphertext using the value of decryption key exponent found
5. If the ciphertext decrypts to some meaningful value then break the loop and print the message


## Example
The public key pair (e, n) has value (17993, 90581). We should determine `d` with the help of the above attack.  
1. Find the continued fraction expansion of `e/N`  
![equation](https://latex.codecogs.com/png.latex?{\frac&space;{e}{N}}={\frac&space;{17993}{90581}}={\cfrac&space;{1}{5&plus;{\cfrac&space;{1}{29&plus;\dots&space;&plus;{\cfrac&space;{1}{3}}}}}}=\left[0,5,29,4,1,3,2,4,3\right])  
2. Thus, the convergents are:  
![equation](https://latex.codecogs.com/png.latex?{\frac&space;{k}{d}}=0,{\frac&space;{1}{5}},{\frac&space;{29}{146}},{\frac&space;{117}{589}},{\frac&space;{146}{735}},{\frac&space;{555}{2794}},{\frac&space;{1256}{6323}},{\frac&space;{5579}{28086}},{\frac&space;{17993}{90581}})  
3. We can iterate over the convergents and check if the denominators of any of them is `d` or not. To check it for each iteration, we must do the following: Take an arbitrary message M, encrypt it using e to give c. Now check if c<sup>d</sup> mod n equals M or not. If not, move on to next iteration but if they match then the corresponding denominator of the convergent is our `d`. For our example, d is 5 which is in fact the denominator of the first convergent.

You can find an implementation of this attack written in sage/python [here](exploit.py)

## References
1. [Wikipedia- Wiener's Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack)

