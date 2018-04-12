# e=3 Bleichenbacher's Signature Forgery
Prerequisites:
1. [RSA Encryption/Decryption](https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption)
2. [RSA Digital Signatures on padded messages using PKCS#1 v1.5](https://github.com/ashutosh1206/Crypton/tree/master/Digital-Signatures/PKCS%231-v1.5-Padded-RSA-Digital-Signature)

The following blog posts/articles have explained e=3 Bleichenbacher's Signature Forgery attack clearly and can be useful:  
1. [Filippo Valsorda's CVE](https://blog.filippo.io/bleichenbacher-06-signature-forgery-in-python-rsa/) --> This was a CVE by Filippo Valsorda on python-rsa module due to fault in implementation of signatures of PKCS#1 v1.5 padded messages 
2. [Karabut's writeup for RSA CTF Challenge, Google CTF Quals 2017](http://karabut.com/google-ctf-2017-quals-rsa-ctf-challenge-writeup.html)
3. [Hal Finney's write-up on Bleichenbacher's Signature Forgery](https://www.ietf.org/mail-archive/web/openpgp/current/msg00999.html)
4. [Interesting explanation on Stack Exchange](https://crypto.stackexchange.com/questions/12688/can-you-explain-bleichenbachers-cca-attack-on-pkcs1-v1-5)
  

Check out the original paper describing the attack by Daniel Bleichenbacher- [http://archiv.infsec.ethz.ch/education/fs08/secsem/bleichenbacher98.pdf](http://archiv.infsec.ethz.ch/education/fs08/secsem/bleichenbacher98.pdf)