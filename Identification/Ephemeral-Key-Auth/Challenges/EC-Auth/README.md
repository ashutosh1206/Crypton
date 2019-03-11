# EC-Auth

1. **Challenge Description**: Service running at `nc 18.191.200.160 1337`
2. **Challenge Writeup**:
   + [My write-up](https://masterpessimistaa.wordpress.com/2018/10/14/inctf-2018-crypto-writeups-part-2/)

## Instructions to host locally
Reference: [Challenge Source- InCTF International](https://github.com/teambi0s/InCTFi/tree/master/2018/Crypto/EC-Auth/ChallHost)

Run the shell script run.sh taken from the above link directory and interact with the service using pwntools' `process` function.

## Directory Contents
1. [ecauth.py](ecauth.py): Authentication script
2. [ecsession.py](ecsession.py): Driver script
