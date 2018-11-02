from Crypto.Util.number import *


def extractmod_eknown(_encrypt, e, limit=4):
    """
    Reference: https://crypto.stackexchange.com/questions/43583/deduce-modulus-n-from-public-exponent-and-encrypted-data

    Function to extract the value of modulus, given value of public key exponent

    :input parameters:
    _encrypt : <type 'function'>      : Function interacting with the server for encryption
    e        : <type 'int' or 'long'> : Public Key exponent
    limit    : <type 'int'>           : number of values to be sent for encryption
    """
    try:
        assert limit <= 4
    except AssertionError:
        print "[+] Limit too big!"
        return -1
    try:
        m_list = [2, 3, 5, 7]
        mod_list = [(bytes_to_long(_encrypt(long_to_bytes(m_list[i])))) - (m_list[i]**e) for i in range(limit)]
        _GCD = mod_list[0]
        for i in range(limit):
            _GCD = GCD(_GCD, mod_list[i])
        return _GCD
    except Exception as ex:
        print "[+] Exception: ", ex

def extractmod_eunknown(_encrypt, limit=4):
    """
    Reference: https://crypto.stackexchange.com/questions/43583/deduce-modulus-n-from-public-exponent-and-encrypted-data

    Function to extract the value of modulus without the value of public key exponent

    :input parameters:
    _encrypt : <type 'function'>      : Function interacting with the server for encryption
    limit    : <type 'int'>           : number of values to be sent for encryption
    """
    try:
        assert limit <= 4
    except AssertionError:
        print "[+] Limit too big!"
        return -1
    try:
        m_list = [2, 3, 5, 7]
        ct_list = [bytes_to_long(_encrypt(long_to_bytes(m_list[i]**2))) for i in range(limit)]
        ct_list2 = [bytes_to_long(_encrypt(long_to_bytes(m_list[i]))) for i in range(limit)]
        assert len(ct_list) == len(ct_list2)
        mod_list = [(ct_list2[i]**2 - ct_list[i]) for i in range(limit)]
        _gcd = mod_list[0]
        for i in mod_list:
            _gcd = GCD(_gcd, i)
        return _gcd
    except Exception as ex:
        print "[+] Exception: ", ex
        return -1
