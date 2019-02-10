# Elliptic Curves

Prerequisites:
1. [Finite Fields](https://en.wikipedia.org/wiki/Finite_field)
2. [Cyclic Groups](https://masterpessimistaa.wordpress.com/2018/01/14/dlp-and-baby-step-giant-step-algorithm/)
3. [Discrete Logarithm Problem](../Discrete-Logarithm-Problem)

To start with Elliptic Curve Cryptography we will first have to see various aspects involved in it. This tutorial is an attempt to help people understand Elliptic Curves better and dive deeper into the concepts as we move forward step by step. This tutorial includes implementation and explanation of the following:
1. Defining Elliptic Curves
2. Mathematics behind Elliptic Curves (painful?)
   + Point Arithmetic
     + Point Addition
     + Point Doubling
   + Scalar Multiplication
     + Double and Add algorithm
     + Montgomery Ladder [To be added]



## Elliptic Curves- definition
Consider the polynomial ![picture2](Pictures/2.gif). All the solutions of this polynomial, when plotted in a graph will look something like this:  
![picture3](Pictures/1.png)  
*Source:  https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/*  

This polynomial has some very interesting properties and a modified version of this polynomial is used for cryptographic purposes. Elliptic Curves provide security with relatively smaller key sizes when compared to other public key systems such as RSA. 

The original polynomial mentioned above is not used directly, as it is favorable to have the curve over a finite set (particularly Finite Fields) than to have it defined over real numbers, for cryptographic purposes. We will see one such popular form of the polynomial which is used as an Elliptic Curve, and can be defined over ![picture1](Pictures/1.gif) as the following:  

> An Elliptic Curve over ![picture1](Pictures/1.gif) with p>3, is the set of all pairs (x, y) in ![picture1](Pictures/1.gif) that satisfy ![picture4](Pictures/4.gif), along with an arbitrary point 0, where ![picture5](Pictures/5.gif)


In this tutorial, we will first define operations on Elliptic Curve over _real numbers_ and then formulate the same for Elliptic Curves over _Finite Fields_.  
We will also see in the next few sections how Elliptic Curve is a better trapdoor function than other existing systems of Public Key Crypto.  



## Notable observations about EC polynomial
1. The curve is symmetric with respect to x-axis:
   + ![picture6](Pictures/6.gif)
2. The curve of the polynomial intersects x-axis at exactly one point, implying that there exists only one real solution to the cubic equation:
   + ![picture7](Pictures/7.gif)



## Point Addition
In this section, we will define addition of two points lying on an Elliptic Curve. Please note that some people use a `dot` operator instead of referring to it as `addition` operation, the operator used to denote the operation could be different, but the operation is still the same.  

Also, `+` is just a notation that we use to denote the operation that we do on two points on an Elliptic Curve, it is not really addition that we do on the two points.  

Assume two points A=(x<sub>1</sub>, y<sub>1</sub>) and B=(x<sub>2</sub>,y<sub>2</sub>) lying on the curve of the polynomial ![picture](Pictures/2.gif). We define C(x<sub>3</sub>, y<sub>3</sub>) as:  
![picture](Pictures/8.gif)  

We can calculate `C` geometrically with the help of following steps:  
> 1. Draw a line from A to B and get a third point of intersection extending the line and on the curve.
> 2. Reflect the point obtained along the x-axis and on the curve. This mirrored point is point C.


To understand it better have a look at this GIF:

![picture](Pictures/9.gif)  
*Source: https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/*

Now that we have defined point addition geometrically, let us formulate the same arithmetically with the help of observations noted from geometric definition of point addition:  
1. We know that A, B, C' (C' is the reflection of point C along x-axis) lie on the curve as well the line joining A=(x<sub>1</sub>, y<sub>1</sub>), B=(x<sub>2</sub>,y<sub>2</sub>). Our approach will be to first calculate the coordinates of C' and then we can simply negate the y-coordinate of C' keeping the x-coordinate as it is to get coordinates of C. We can write:  
   + ![picture](Pictures/2.gif)
   + For (x<sub>1</sub>, y<sub>1</sub>), ![picture](Pictures/10.gif), where `m` is the slope of the line connecting A and B.
   + Thus, we have
     + ![picture](Pictures/11.gif)
   + We know that (x-x<sub>1</sub>) and (x-x<sub>2</sub>) are factors of the above cubic equation obtained, and also we can write from [Vieta's Formula](https://en.wikipedia.org/wiki/Vieta%27s_formulas) that for a polynomial `P(x)` defined as: ![picture](Pictures/12.gif), sum of the roots ![picture](Pictures/13.gif). Hence we can write for a cubic polynomial that ![picture](Pictures/14.gif) which in case of our polynomial can be written as ![picture](Pictures/15.gif). We know x<sub>1</sub>, x<sub>2</sub> and m<sup>2</sup> so we can calculate x<sub>3</sub> as:  
     + ![picture](Pictures/16.gif) --> Using this formula we can calculate the x-coordinate of C'
   + Now that we have the x-coordinate of C', we can use it to calculate the y-coordinate of C' as well. Note that point C does not lie on the line joining A and B, but the reflection of point C on x-axis lies on the line joining A and B ie. point C'; the x-coordinate of point C remains the same, while the y-coordinate is just negated. Since point A and C' lie on the same line, we can write:
     + ![picture](Pictures/17.gif)

Now that we have calculated (x, y) coordinates of C', we can write coordinates of C as:  
> ![picture](Pictures/18.gif)  
> Notice that we added (mod p) in calculation as our curve is defined over the Finite Field ![picture](Pictures/1.gif) and not over Real Numbers


You can find an implementation of the above discussed method in python here: [ellipticcurve.py](ellipticcurve.py) and in sage here(lesser lines of code): [ellipticcurve.sage](ellipticcurve.sage)


## Point Doubling
Point Doubling is similar to Point Addition, just that the formula for calculating slope is different, rest of the formulae for getting the coordinates of x<sub>3</sub> and y<sub>3</sub> are the same. We will first define point doubling geometrically and then define it arithmetically. Please note here `doubling` is just a notation, the operation that takes place on point lying on the curve is very different from normal doubling.  

Consider a point P=(x<sub>3</sub>, y<sub>3</sub>) that we want to `double`. We can calculate 2P with the help of following steps:
> 1. Draw a tangent on the curve through P and obtain a second point of intersection between the curve and the line.
> 2. Reflect the point obtained along the x-axis and on the curve. This mirrored point is 2P.


![picture](Pictures/2.jpg)  


We can also understand it using Point Addition: Consider addition two points P and Q on an Elliptic Curve, as Q approaches P, the line joining the two points to `add` these points approaches closer and as Q becomes very very close to P, the line becomes a tangent at point P.  

Formula for slope will be different, as we have only one point on the curve and we want to compute the slope of its tangent, let us see how we can do it:
1. We know that ![picture](Pictures/2.gif). Differentiating both sides of this equation with respect to x, we get:
2. ![picture](Pictures/20.gif)
3. Thus, with the given point (x<sub>1</sub>, y<sub>1</sub>), we can write `m` as:
   + ![picture](Pictures/21.gif), where `m` is slope of the tangent passing through the point P

Arithmetically, we can express coordinates of 2P as:  
> ![picture](Pictures/19.gif)  
> Here m is the slope of the tangent passing through P


You can find an implementation of the above method in python here: [ellipticcurve.py](ellipticcurve.py) and in sage here(lesser lines of code): [ellipticcurve.sage](ellipticcurve.sage)

## Scalar Multiplication
There are two algorithms for implementing scalar multiplication in Elliptic Curves:
1. Double and Add algorithm
2. Montgomery Ladder

We will see how to implement each algorithm and also discuss why Montgomery ladder is preferred over Double and Add algorithm.

### Double and Add Algorithm
This is a very simple algorithm for multiplication of a point with a scalar. Let us try to first understand multiplication of two scalars `a` and `b` using double and add, and then apply the same logic for points on an Elliptic Curve.  
Suppose you want to multiply 5 = (101)<sub>2</sub> by 11 = (1011)<sub>2</sub>
1. We can write: 5\*11 = 5 \* (1\*2<sup>0</sup> + 1\*2<sup>1</sup> + 0\*2<sup>2</sup> + 1\*2<sup>3</sup>)
   + 5\*11 = 5\*1\*2<sup>0</sup> +  5\*1\*2<sup>1</sup> +  5\*0\*2<sup>2</sup> +  5\*1\*2<sup>3</sup>
2. For each term starting from the left, corresponding bit of `b` (ie equal to 11 in our example) is multiplied with a*2<sup>i</sup>, where i = 0,...,n (`n` is number of bits of `b` minus 1)
   + All the terms are then added together to give the result

Let us implement this algorithm for multiplying two scalars `a` and `b`:
```python
def doubleandadd(a, b):
    res = 0
    addend = a
    for i in bin(b)[2:][::-1]:
        if i == "1":
            res = res + addend
        addend *= 2
    return res
```

We can apply the same for Elliptic Curves, the only difference is that instead of `a` we have a point `P` lying on an Elliptic Curve `E`:

```python
from sage.all import *
# Declaring parameters of Elliptic Curve
# Select appropriate values of p, a, b

# Declaring a Weierstrass Curve
E = EllipticCurve(GF(p), [a, b])

def doubleandadd(E, P, b):
    # P is a point on the Elliptic Curve E

    # (0:1:0) are projective coordinates of arbitrary point at infinity
    res = E((0, 1, 0))
    addend = P
    for i in bin(b)[2:][::-1]:
        if i == "1":
            res = res + addend
        addend = addend * 2
    return res
```
[Projective coordinates of points on Elliptic Curves](https://math.stackexchange.com/questions/1973640/elliptic-curve-point-op-zero-point-p)

## Resources
There are some pretty cool resources on ECC which you can refer:  
1. [Andrea Corbellini- Gentle Introduction to Elliptic Curves](https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction)
2. [Andrea Corbellini- Finite Fields and Discrete Logarithms](https://andrea.corbellini.name/2015/05/23/elliptic-curve-cryptography-finite-fields-and-discrete-logarithms/)
3. [Nick Sullivan- Primer on Elliptic Curves](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)
4. [Introduction to Cryptography by Christof Paar- Introduction to Elliptic Curves](https://www.youtube.com/watch?v=vnpZXJL6QCQ)
5. [Introduction to Cryptography by Christof Paar- Elliptic Curve Cryptography](https://www.youtube.com/watch?v=zTt4gvuQ6sY)



## References
1. Picture/GIF reference: https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/
