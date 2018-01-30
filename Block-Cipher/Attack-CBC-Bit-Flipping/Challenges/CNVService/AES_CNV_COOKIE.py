from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto.Cipher import AES
from time import ctime
from Secret import __HIDDEN__, __SECRET__

BLOCK_SIZE = 16

pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * \
                chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

def xor(dest, src):
    if len(dest) == 0:
        return src
    elif len(src) == 0:
        return dest
    elif len(dest) >= len(src):
        return ''.join(chr(ord(dest[i])^ord(src[i])) for i in range(len(src)))
    else:
        return ''.join(chr(ord(dest[i])^ord(src[i])) for i in range(len(dest)))


class AES_CNV:

    def __init__(self, key):
        assert len(key) == BLOCK_SIZE
        self.key = key

    def encrypt(self, plain_text, iv):
        assert len(iv) == 16
        plain_text = pad(plain_text)
        assert len(plain_text)%BLOCK_SIZE == 0
        cipher_text = ''
        aes = AES.new(self.key, AES.MODE_ECB)
        h = iv
        for i in range(len(plain_text)//BLOCK_SIZE):
            block = plain_text[i*16:i*16+16]
            block = xor(block, h)
            cipher_block = aes.encrypt(block)
            cipher_text += cipher_block
            h = md5(cipher_block).digest()
        return iv+cipher_text

    def decrypt(self, cipher_text):
        assert len(cipher_text)%BLOCK_SIZE == 0
        iv = cipher_text[:16]
        cipher_text = cipher_text[16:]
        aes = AES.new(self.key, AES.MODE_ECB)
        h = iv
        plain_text = ''
        for i in range(len(cipher_text)//BLOCK_SIZE):
            block = cipher_text[i*16:i*16+16]
            plain_block = aes.decrypt(block)
            plain_block = xor(plain_block, h)
            plain_text += plain_block
            h = md5(block).digest()
        return unpad(plain_text)

class Cookie:

    def __init__(self, key):
        assert len(key) == BLOCK_SIZE
        self.key = key

    def register(self, name, username):
        name = pad(name)
        iv = xor(name, md5(__HIDDEN__).digest())
        cookie = "CNVService" + "*" + "user="+ username + "*" + ctime() + "*" + __SECRET__
        aescnv = AES_CNV(self.key)
        cookie = aescnv.encrypt(cookie, iv)
        return b64encode(cookie)

    def authentication(self, cookie):
        cookie = b64decode(cookie)
        name = cookie[:16]
        name = xor(name, md5(__HIDDEN__).digest())
        if ord(name[-1]) < 16:
            name = unpad(name)
        aescnv = AES_CNV(self.key)
        cookie = aescnv.decrypt(cookie)
        info = cookie.split("*")
        if info[0] != "CNVService":
            return None, None, None
        elif info[-1] != __SECRET__:
            return None, None, None
        elif "user=" != info[1][:5]:
            return None, None, None
        elif len(info[1].split("=")) == 2:
            return name, info[1].split("=")[1], info[2]
        else:
            return None, None, None
