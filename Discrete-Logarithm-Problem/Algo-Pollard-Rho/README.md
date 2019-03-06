# Pollard Rho Algorithm

**Prerequisites**:
1. [Discrete Logarithm Problem](https://github.com/ashutosh1206/Crypton/tree/master/Discrete-Logarithm-Problem)

**Pollard Rho Algorithm** can give a unique solution in cases where order of the group, over which the DLP is defined, is a prime number. First, let us define our DLP over the Cyclic Group `G` = ![picture](Pictures/1.gif) having order `n`.

You can refer to section 3.6.3 of chapter-3 from Handbook of Applied Cryptography to read in detail about Pollard Rho Algorithm

I implemented this algorithm in python here (with appropriate explanation): [pollardrho.py](pollardrho.py)


## References
1. [Wikipedia- Pollard Rho for DLP](https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm_for_logarithms)
2. [Handbook of Applied Cryptography](http://cacr.uwaterloo.ca/hac/about/chap3.pdf)
