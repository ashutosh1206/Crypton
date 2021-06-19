from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA


def lsbitoracle(flag_enc, _decrypt, e, N):
    """
    Reference: https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack

    Function implementing LSBit Oracle Attack

    :parameters:
        flag_enc   : str
                    Ciphertext you want to decrypt
        _decrypt   : function
                    Function interacting with the server for decryption
        e          : int/long
                    Public Key exponent
        N          : long
                    Public Key Modulus

    Returns -1 in case of any Exception
    """
    flag = ""
    i = 1
    lower_limit = 0
    upper_limit = 1
    denominator = 1
    for i in range(1, N.bit_length()+1):
        chosen_ct = long_to_bytes((bytes_to_long(flag_enc)*pow(2**i, e, N)) % N)
        output = _decrypt(chosen_ct)
        delta = upper_limit - lower_limit
        upper_limit *= 2
        lower_limit *= 2
        denominator *= 2
        if ord(output[-1]) == 0:
            upper_limit -= delta
        elif ord(output[-1]) == 1:
            lower_limit += delta
        else:
            return -1
        i += 1
    flag = N * lower_limit / denominator
    return long_to_bytes(flag)
