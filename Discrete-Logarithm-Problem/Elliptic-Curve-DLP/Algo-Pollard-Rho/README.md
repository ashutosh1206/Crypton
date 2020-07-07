# Pollard Rho Algorithm for solving ECDLP

**Prerequisites**:
1. [Elliptic Curve Discrete Logarithm Problem](../../Elliptic-Curve-DLP/)

**Pollard Rho Algorithm** for solving ECDLP will give a unique solution in cases where order of the group, over which the DLP is defined, is a prime number. Otherwise, it can give multiple solutions.


To find any two pairs ![picture](Pictures/2.gif) & ![picture](Pictures/3.gif) such that  
![picture](Pictures/1.gif)

Once we have these pairs, we can write:  
![picture](Pictures/4.gif)

Let base point P have order = n. Then we can write:  
![picture](Pictures/5.gif)  
![picture](Pictures/6.gif), provided GCD((B-b), n) == 1

But the problem is, **how do we calculate (a, b) and (B, b)**?

Brute Forcing such pairs will be of the order ![picture](Pictures/7.gif) which is even larger than the
brute force algorithm for solving ECDLP: ![picture](Pictures/8.gif).

We can use Floyd's Cycle Finding Algorithm to reduce the complexity!
Have a look at how the Cycle Finding algorithm can be efficiently used to solve ECDLP:

![picture](https://andrea.corbellini.name/images/tortoise-hare.gif)  
*Source: https://andrea.corbellini.name/2015/06/08/elliptic-curve-cryptography-breaking-security-and-a-comparison-with-rsa/*

Basically, the algorithm is
1. Initially select any integral values for the two pairs ![picture](Pictures/9.gif), ![picture](Pictures/10.gif)
2. Keep calculating ![picture](Pictures/11.gif) and ![picture](Pictures/12.gif), ![picture](Pictures/13.gif) until ![picture](Pictures/14.gif)
   + Check if ![picture](Pictures/15.gif),
     + If true, then start again from (1)
     + If false, then return ![picture](Pictures/16.gif) as `x`

## How to calculate ![picture](Pictures/17.gif), ![picture](Pictures/18.gif), ![picture](Pictures/19.gif)

![picture](Pictures/20.gif)

![picture](Pictures/11.gif)

![picture](Pictures/21.gif)

```
Function f(x):

                      /----------------------------------------------------------|
                     /    X_i + Q = a_i*P       + (b_i + 1)*Q   , X_i[0] in S_1  |
func_f() ~ f(X_i) = /     2*X_i   = (2*a_i)*P   + (2*b_i)*Q     , X_i[0] in S_2  |
                    \     X_i + P = (a_i + 1)*P + b_i*Q         , X_i[0] in S_3  |
                     \-----------------------------------------------------------|

```

**Note**: Since ![picture](Pictures/22.gif) is a point and not an integer, we simply partition using x-coordinate of ![picture](Pictures/22.gif)

We can conclude from the above formula that the value of ![picture](Pictures/23.gif) depends upon
the set (S_1, S_2, S_3) to which ![picture](Pictures/22.gif) belongs.

Now, we need to calculate values of ![picture](Pictures/18.gif) and ![picture](Pictures/19.gif). Both of them will also
depend upon the set(S_1, S_2, S_3) to which X_i belongs.

```
Function g(x) and h(x):

                       /--------------------------------|
                      /    a_i         , X_i[0] in S_1  |
func_g() ~ a_(i+1) = /     2*a_i       , X_i[0] in S_2  |
                     \     (a_i + 1)   , X_i[0] in S_3  |
                      \---------------------------------|

                       /--------------------------------|
                      /    (b_i + 1)   , X_i[0] in S_1  |
func_h() ~ b_(i+1) = /     2*b_i       , X_i[0] in S_2  |
                     \     b_i         , X_i[0] in S_3  |
                      \---------------------------------|
```

I implemented the algorithm in python/sage (with appropriate comments/explanation) here: [pollardrho.py](pollardrho.py)


# References
1. [Andrea Corbellini- Pollard's Rho](https://andrea.corbellini.name/2015/06/08/elliptic-curve-cryptography-breaking-security-and-a-comparison-with-rsa/)
2. Section 3.6.3 of [chapter-3 from Handbook of Applied Cryptography](http://cacr.uwaterloo.ca/hac/about/chap3.pdf)
