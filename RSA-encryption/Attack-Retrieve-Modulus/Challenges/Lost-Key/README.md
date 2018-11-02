# Lost-Key

1. **Challenge Description**: I lost my public key. Can you find it for me?
  + `nc 18.179.251.168 21700`
2. **Challenge Writeup**
  + [CTFtime](https://ctftime.org/task/6888)
  + [My exploit script](https://github.com/ashutosh1206/Crypto-CTF-Writeups/blob/master/2018/HITCON-CTF/Lost-Key/exploit.py)

## Instructions to host locally
Run the shell script [run.sh](run.sh) and interact with the service using pwntools' `process` function. For more information, checkout the script I wrote to solve the challenge locally [exploit.py](exploit.py).

## Directory Contents
1. [rsa.py](rsa.py): encryption script
2. [flag](flag): flag file (Not public, only for hosting purposes)
3. run.sh
4. [exploit.py](exploit.py): exploit script to solve the challenge locally
