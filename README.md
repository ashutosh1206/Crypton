# Crypton
  

Crypton is an educational library to **learn** and **practice** Offensive and Defensive Cryptography. It is basically a collection of explanation and implementation of all the existing vulnerabilities and attacks on various Encryption Systems (Symmetric and Asymmetric), Digital Signatures, Message Authentication Codes and Authenticated Encryption Systems. Each attack is also supplemented with example challenges from "Capture The Flag" contests and their respective write-ups. Individuals who are already acquainted (or are into CTFs) with this field can use Crypton as a tool to solve challenges based on a particular existing vulnerability.  
  
The library will be continuously updated with attack explanations and CTF challenges!
  
There are different sections in this README:  
* Motivation- What motivated me to create this library
* Library Structure- Directory structure of Crypton
* Domain Coverage- What all cryptosystems and attacks are covered in this library
* Future Plans/ TODO- Attacks/concepts that are to be included soon
  
  

---
## Motivation
Help CTF players and individuals interested in the field of Cryptography a platform for learning attacks in crypto and provide a platform for experienced CTF players to practice challenges systematically divided into attacks associated with different sub-domains in crypto. Illustrate through various attack explanations how proper implementation of protocols is crucial.
  
  

---
## Library Structure
  
  

![picture](Pictures/1.png)  
  
  
---

## Domain Coverage
  
#### 1. Block Ciphers

| S.No. | Topic                       | Explanation                                                                                     | Exploit File | Challenge# |
|-------|:---------------------------:|:-----------------------------------------------------------------------------------------------:|:------------:|:----------:|
| 1     | [Block Cipher Basics](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher#block-cipher)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/README.md)</li></ul>| <ul><li>- [ ] </li></ul>         | <ul><li>- [ ] </li></ul>   |
| 2     | [Modes of Encryption](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Mode-of-Encryption)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Mode-of-Encryption/README.md)</li></ul>| <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |
| 3     | [Block Size Detection](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher#block-size-detection)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher#block-size-detection)</li></ul>| <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |
| 4     | [Mode Detection](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher#mode-detection)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher#mode-detection)</li></ul>| <ul><li>- [ ] </li></ul> | <ul><li>- [ ] </li></ul> |
| 5     | [ECB Byte at a Time](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-ECB-Byte-at-a-Time)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-ECB-Byte-at-a-Time/README.md)</li></ul>| <ul><li>- [ ] </li></ul> | <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-ECB-Byte-at-a-Time/Challenges) </li></ul> |
| 6     | [CBC IV Detection](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/CBC-IV-Detection)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/CBC-IV-Detection/README.md) </li></ul>| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/CBC-IV-Detection/example.py) </li></ul> | <ul><li>- [ ] </li></ul> |
| 7     | [CBC Bit Flipping Attack](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Bit-Flipping)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-CBC-Bit-Flipping/README.md) </li></ul>| <ul><li>- [ ] </li></ul> | <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Bit-Flipping/Challenges) </li></ul> |
| 8     | [CBC Byte at a Time](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Byte-at-a-Time)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-CBC-Byte-at-a-Time/README.md) </li></ul>| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-CBC-Byte-at-a-Time/exploit.py) </li></ul> |  <ul><li>- [ ] </li></ul> |
| 9     | [CBC Padding Oracle Attack](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Padding-Oracle)| <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-CBC-Padding-Oracle/README.md) </li></ul>|  <ul><li>- [ ] </li></ul> |  <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CBC-Padding-Oracle/Challenges) </li></ul> |
| 10    | [CTR Bit Flipping](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CTR-Bit-Flipping)| ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/blob/master/Block-Cipher/Attack-CTR-Bit-Flipping/README.md) </li></ul>|  <ul><li>- [ ] </li></ul> |  <ul><li>- [x] [\[link\]](https://github.com/ashutosh1206/Crypton/tree/master/Block-Cipher/Attack-CTR-Bit-Flipping/Challenges) </li></ul> |
  
  