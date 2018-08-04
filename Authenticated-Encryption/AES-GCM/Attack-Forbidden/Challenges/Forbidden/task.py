from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
#from secret import key


def encrypt(iv, key, plaintext, associated_data):
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()
    encryptor.authenticate_additional_data(associated_data)
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (ciphertext, encryptor.tag)


def decrypt(key, associated_data, iv, ciphertext, tag):
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()
    decryptor.authenticate_additional_data(associated_data)

    return decryptor.update(ciphertext) + decryptor.finalize()


iv = "9313225df88406e555909c5aff5269aa".decode('hex')
key = "\x1eh_[Q\xa0\xae\xfb\x9b,\x11\x85\xfb\xa6\xbe\xaa"

ciphertext1, tag1 = encrypt(iv, key, "From: John Doe\nTo: John Doe\nSend 100 BTC", "John Doe")
ciphertext2, tag2 = encrypt(iv, key, "From: VolgaCTF\nTo: VolgaCTF\nSend 0.1 BTC", "VolgaCTF")
ciphertext3, tag3 = encrypt(iv, key, "From: John Doe\nTo: VolgaCTF\nSend ALL BTC", "John Doe")
