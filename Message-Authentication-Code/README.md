# Message Authentication Code

MACs are a type of keyed-hashing algorithms mostly derived from already-existing encryption/hashing algorithms to provide authenticity and integrity to the message that the sender is trying to send. MACs provide authenticity and integrity by computing a value known as the **Authentication Tag** T = MAC(k, M), where k is the key and M is the message whose MAC we want to generate. When communication is supposed to happen between the sender and the receiver, the following happens:
1. Alice (sender) and Bob (receiver) both agree upon a key value k
2. Alice sends message M along with its authentication tag T = MAC(k, M) over the channel
3. Bob receives the message and calculates if MAC(k, M) == T or not, thus preserving the **integrity** of the message
4. Since only Alice knows about the key k, Bob can be sure that the message actually came from the sender itself, thus providing **authenticity**    
   
   

## Security analysis of MACs
The key used for generating the MAC is to be always kept secret between the sender and the receiver. When an attacker is able to generate a valid message-tag pair without knowing the key, it is called **MAC-Forgery**. List of attacks:
1. Replay Attack
2. Length Extension Attacks on Secret-Prefix Construction
3. (In)security with different key lengths in Secret-Prefix-Construction
4. Collision Attack on Secret-Suffix-Construction
5. Generic Forgery-Attack on Hash based MACs (HMACs)
6. CBC-MAC Forgery
  
