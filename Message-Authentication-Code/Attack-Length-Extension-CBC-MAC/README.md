# Length Extension Attack on CBC-MAC

Prerequisites:
1. [CBC-MAC](https://en.wikipedia.org/wiki/CBC-MAC) 

Using the attack described here, the attacker can generate a valid **Authentication Tag** of message M1 || M2 given MAC(M1), without having the knowledge of key k. Note that M2 can selected purely by choice of the attacker.  
  
Case scenario: 
* Code running on the server that allows the user to give a string as an input
* Checks if the string is equal to M1 || M2, if not then it  
    * Calculates CBC-MAC of the input string  
    * Returns the Authentication Tag of the message  
    Otherwise,
    * Returns a null string  

As an attacker, we want to get the authentication tag of M1 || M2, without sending M1 || M2 as the input. Let us see how we can do it.  
  
  
## The vulnerability and exploit
![image](https://i.imgur.com/upHacu8.png)
There are two cases that we have to take into consideration while implementing the exploit: case when the IV is a null string and the other when IV is not a null string.  
* Case 1: When IV is a null string: We can get the authentication tag of M1 || M2 by the following steps:
    * Get the authentication tag of message M1 = MAC(M1)
    * XOR it with M2, and send the result as input to the code running on the server.
    * The output will be MAC(M1 || M2)
* Case 2: When IV is not null: It's value will most probably be given, we can get the authetication tag of M1 || M2 by the following steps:
    * Get the authentication tag of message M1 = MAC(M1)
    * XOR it with (M2 xor IV) and send the result as input to the code running on the server
    * The output will be MAC(M1 || M2)

## Example
Check out the example script [here](CBC-Length-Extension.py).

