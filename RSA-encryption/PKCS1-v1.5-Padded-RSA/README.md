# RSA Encryption using PKCS#1-v1.5 padding
  
Prerequisites:
1. [RSA Encryption/Decryption](https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption)
  

This section covers RSA encryption using PKCS1-v1.5 padding. Padding was introduced in RSA to ensure security against attacks such as cube-root (we introduce padding to ensure the ciphertext wraps around the modulus), [Coppersmith's Attack](https://github.com/ashutosh1206/Crypton/tree/master/RSA-encryption/Attack-Coppersmith), etc. 