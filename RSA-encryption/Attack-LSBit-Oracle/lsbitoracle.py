from Crypto.Util.number import long_to_bytes, bytes_to_long
from Crypto.PublicKey import RSA


def lsbitoracle(flag_enc, _decrypt, e, N, upper_limit, lower_limit):
    """
    Reference: https://crypto.stackexchange.com/questions/11053/rsa-least-significant-bit-oracle-attack

    Function implementing LSBit Oracle Attack

    *Warning*: Function does not return the last byte of the final plaintext

    :parameters:
        flag_enc   : str
                    Ciphertext you want to decrypt
        _decrypt   : function
                    Function interacting with the server for decryption
        e          : int/long
                    Public Key exponent
        N          : long
                    Public Key Modulus
        upper_limit: long
                    Maximum value of corresponding plaintext of flag_enc
        lower_limit: long
                    Minimum value of corresponding plaintext of flag_enc

    Since the attack messes up with the last byte of the plaintext, lsbitoracle
    function returns only flag[:-1]. It returns -1 in case of any Exception
    """
    flag = ""
    i = 1
    while lower_limit < upper_limit:
        chosen_ct = long_to_bytes((bytes_to_long(flag_enc)*pow(2**i, e, N)) % N)
        output = _decrypt(chosen_ct)
        if ord(output[-1]) == 0:
            upper_limit = (upper_limit + lower_limit)/2
        elif ord(output[-1]) == 1:
            lower_limit = (lower_limit + upper_limit)/2
        else:
            return -1
        i += 1
    # clearing the last byte from the flag
    flag = lower_limit & (~0xff)
    return long_to_bytes(flag)
