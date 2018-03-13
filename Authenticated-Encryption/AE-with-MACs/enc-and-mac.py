from Crypto.Cipher import AES
from os import urandom
from Crypto.Util.number import *

key = urandom(16)
iv = urandom(16)
key2 = urandom(16)