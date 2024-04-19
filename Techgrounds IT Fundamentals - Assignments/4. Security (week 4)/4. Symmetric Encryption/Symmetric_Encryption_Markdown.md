# [Symmetric Encryption]
Either data at rest, or in motion, encryption is an important tool in securing it. A lot of what you do on your computer and Internet is encrypted. 
Of all the ciphers we've come up with as humans to encode information, most of them are symmetric ciphers. Most notably the Caesar cipher.

## Key-terms
Encryption: Encryption is converting human-readable plaintext to incomprehensible text, known as ciphertext. By way of mathematical values (a cryptographic key) the plaintext is converted to incomprehensible text, and back into plaintext. 

Cipher: Ciphers are encryption algorithms that encrypt and decrypt data.

Symmetric cipher: A symmetric cipher uses the same key for encryption and decryption.



## Assignment
### Used sources
[Source 1: What is encryption?](https://www.cloudflare.com/learning/ssl/what-is-encryption/)

[Source 2: What is a cypher?](https://www.hypr.com/security-encyclopedia/cipher)

[Source 3: What is a symmetric cipher?](https://www.hypr.com/security-encyclopedia/symmetric-cipher)

[Source 4: Historic ciphers](https://lockhouse.co.uk/5-classical-ciphers-history/)

### Experienced problems


### Result
Tasks:

-	Find one more historic cipher besides the Caesar cipher.
    -	Scytale
        -	The scytale, a cryptographic device from the 3rd century BCE, was a rod with a piece of parchment wound around it. While it is wound a message is written on it. When the parchment is unwound, the text becomes a random sequence that is reverted back to coherent text when wound around a rod of the same size used to write the text.
-	Find two digital ciphers that are being used today.
1.	AES (Advanced Encryption Standard): An algorithm trusted as the standard by the U.S. Government as well as numerous organisations. It makes use of 128, 192, and 256-bit ciphers.
2.	Blowfish: Both AES and Blowfish were designed to replace the original Data Encryption Standard (DES). It works by splitting messages into 64 bit blocks, after which it encrypts each block. It is known for its tremendous speed and overall effectiveness. It is also freely available in the public domain.  
-	Send a symmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key you share with them. Try to think of a way to share this encryption key without revealing it to everyone. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the shortcomings of symmetric encryption for sending messages.
    -	I’ve posted an encrypted message through a textfile with a message attached to the post that contains the password. The message was “some might say this isnt a text. But I assure you, it is.” Along with a link to download blowfish, which I used to encrypt the text. The password is “somemightsaythisisntatext”. I tried to emphasise it by leaving out any capitalisation and interpunction in the password sentence.
    -	One of the shortcomings I’m noticing with this assignment is that it can be quite a hassle to get people to find out what the keys are to decrypt a message without anyone else finding out. My password for instance, is not specific to my group. Anyone could figure it out. Either way, it creates an extra hassle that isn’t quite efficient.



