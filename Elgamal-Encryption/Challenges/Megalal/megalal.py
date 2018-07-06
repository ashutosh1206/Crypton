#!/usr/bin/env python2

import binascii
import base64
import random

from secrets import g, p, x, h, flag

def xgcd(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

def modinv(b, n):
    g, x, _ = xgcd(b, n)
    if g == 1:
        return x % n

def enc(m):
    M = int(binascii.hexlify(m), 16)
    assert len(bin(M)) < len(bin(p)), 'm too long'

    y = random.SystemRandom().randint(0, p-1)
    c1 = pow(g, y, p)
    c2 = (M * pow(h, y, p) ) % p 

    return c1, c2

def dec(c1, c2):
    s = pow(c1, x, p)
    M = (c2 * modinv(s, p)) % p
    
    return str(binascii.unhexlify('{:x}'.format(M)))

def login():
    c = raw_input('Please input your access token: ').split('_')
    c1 = int(c[0], 16)
    c2 = int(c[1], 16)
    user, role = dec(c1, c2).split('#')
    print('\nWelcome {}!'.format(user))
    print('Your role is \'{}\'.\n'.format(role))
    if role == 'overlord':
        print('Here\'s your flag: {}'.format(flag))
    print('That\'s all, nothing else happening here.')

def register():
    username = raw_input('Your username: ')
    role = raw_input('Your role: ')

    if role == 'overlord':
        print('nope, you\'re not the overlord...')
        return
    c = enc('%s#%s' % (username, role))
    token = '{:x}_{:x}'.format(c[0], c[1])

    print('Here is your access token:\n{}'.format(token))

if __name__ == '__main__':
    print('What do you want to do?')
    print('[1] Login')
    print('[2] Register')
    choice = raw_input('> ')
    try:
        if choice == '1':
            login()
        elif choice == '2':
            register()
    except:
        print('something went wrong...')
