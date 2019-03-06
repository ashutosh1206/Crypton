# Pohlig Hellman Algorithm

**Prerequisites**:
1. [Discrete Logarithm Problem](https://github.com/ashutosh1206/Crypton/tree/master/Discrete-Logarithm-Problem)

**Pohlig Hellman Algorithm** is applicable in cases where order of the group, over which DLP is defined, is a smooth number (ie. the number that can be factored into small prime numbers). First, let us define our DLP over the Cyclic Group `G` = ![picture](Pictures/1.gif) having order `n`.

There are different variations to Pohlig-Hellman algorithm that can be applied in different conditions:
1. When **order** of a group **is a power of 2 only** ie. n = 2<sup>e</sup>
2. When **order** of a group **is a power of a prime** ie. n = p<sup>e</sup>, where `p` is a prime number
3. **General algorithm** ie. n = p<sub>1</sub><sup>e<sub>1</sub></sup> p<sub>2</sub><sup>e<sub>2</sub></sup> p<sub>3</sub><sup>e<sub>3</sub></sup>... p<sub>r</sub><sup>e<sub>r</sub></sup>

## Order of a group is a power of 2
![picture](Pictures/2.png)  
*Source: https://crypto.stackexchange.com/questions/34180/discrete-logarithm-problem-is-easy-in-a-cyclic-group-of-order-a-power-of-two*

I implemented this algorithm in python here: [ph_orderp2.py](ph_orderp2.py)

So if you have a group whose order is a power of 2, you can now solve the DLP in ![picture](Pictures/2.gif), where `e` is the exponent in the group order n = 2<sup>e</sup>.

## Order of a group is a power of a prime number

**Source**: [http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf](http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf)

I implemented this algorithm in python here: [ph_orderpp.py](ph_orderpp.py)

## General Algorithm

**Source**: [http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf](http://anh.cs.luc.edu/331/notes/PohligHellmanp_k2p.pdf)

I implemented this algorithm in python/sage here:
[pohlig_hellman.py](pohlig_hellman.py)
