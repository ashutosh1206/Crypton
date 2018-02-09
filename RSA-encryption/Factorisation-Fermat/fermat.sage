def basic_fermat(n):
    a = ceil(sqrt(n))
    b2 = a^2 - n
    while not is_square(b2):
        a += 1
        b2 = a^2 - n
    return (a-sqrt(b2), a+sqrt(b2))  
    