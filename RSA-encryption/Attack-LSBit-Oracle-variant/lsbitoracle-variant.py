from Crypto.Util.number import long_to_bytes, bytes_to_long, inverse

def lsbitoracle_variant(flag_enc, _decrypt, e, N, len_flag):
    """
    Function implementing a variant of LSBit Oracle Attack
    Time complexity is O(len_flag) where len_flag is the length of the flag in bits

    :parameters:
        flag_enc : str
                    Ciphertext we want to decrypt
        _decrypt : function
                    Function interacting with the remote service for decryption
        e        : int/long
                    Public Key exponent
        N        : long
                    Public Key modulus
        len_flag : int
                    Length of plaintext in bits (for eg. 128 bit long flag)

    Function returns -1 in case of any Exception, with appropriate error message
    """
    output = _decrypt(flag_enc)
    assert output == "\x01" or output == "\x00"
    flag = bin(ord(output))[2:]

    for i in range(1, len_flag):
        temp_cal = 2**i
        try:
            assert GCD(temp_cal, N) == 1
        except:
            print "[-] GCD(2**i, N) != 1, obtained one factor of N successfully"
            return -1
        inv = inverse(temp_cal, N)
        chosen_ct = long_to_bytes((bytes_to_long(flag_enc)*pow(inv, e, N)) % N)
        output = _decrypt(chosen_ct)
        try:
            assert output == "\x01" or output == "\x00"
        except:
            print "[-] Unusual output obtained. Exiting..."
            return -1
        # Compute i-th bit of plaintext based on the output obtained above
        flag_char = (ord(output) - (int(flag, 2)*inv) % N) % 2
        # Prepend i-th bit calculated to the plaintext string
        flag = str(flag_char) + flag
        if len(flag) % 8 == 0:
            print "Plaintext recovered till now: ", long_to_bytes(int(flag, 2))
    return long_to_bytes(int(flag, 2))
