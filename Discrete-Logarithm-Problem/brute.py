def brute_dlp(g, y, p):
    """
    Brute Force algorithm to solve DLP. Use only if the group is very small.
    Includes memoization for faster computation

    :parameters:
        g : int/long
                Generator of the group
        y : int/long
                Result of g^x % p
        p : int/long
                Group over which DLP is generated. Commonly p is a prime number
    """
    mod_size = len(bin(p-1)[2:])

    print "[+] Using Brute Force algorithm to solve DLP"
    print "[+] Modulus size: " + str(mod_size) + ". Warning! Brute Force is not efficient\n"

    sol = pow(g, 2, p)
    if y == 1:
        return p-1
    if y == g:
        return 1
    if sol == y:
        return 2
    i = 3
    while i <= p-1:
        sol = sol*g % p
        if sol == y:
            return i
        i += 1
    return None

if __name__ == "__main__":
    try:
        assert pow(2, brute_dlp(2, 25103, 50021), 50021) == 25103
        assert pow(2, brute_dlp(2, 147889, 200003), 200003) == 147889
        print brute_dlp(2, 4, 19)
    except:
        print "[+] Function inconsistent and incorrect, check the implementation"
