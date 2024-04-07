# [Asymmetric Encryption]
Where symmetrical encryption (see previous assignment) uses only 1 key, assymetrical encryption uses 2: a public key, and a private key. This solves the problem of anyone having your key being able to decrypt your message.
I'm not yet done with the second source, but the added level of security of having two keys really feels negated by having one be public. That sounds like it effectively becomes one key to hack, just like with symmetric encryption. Hopefully the article will make things clear.

## Key-terms
Asymmetrical encryption: Encryption using a public key, and a private key. 

## Assignment
### Used sources
[Source 1: What is asymmetric encryption?](https://www.cloudflare.com/learning/ssl/what-is-asymmetric-encryption/#:~:text=As%20the%20name%20implies%2C%20asymmetric,decrypted%20with%20the%20private%20key.)

[Source 2: What is asymmetric encryption?](https://www.okta.com/identity-101/asymmetric-encryption/)

### Experienced problems
I'm having a little trouble understanding how asymmetric encryption is more secure. It undoubtedly is, since it's so widely used, but when I use the encryption tools, I get both keys. I still have to send the message and private/public key to the receiver, which can be stolen and used. I'm going to do some more reading.
    Now I get it. In this exercise, I'm making the keys, and encrypting the message. In the real world there would already be a public key that the recipient has made. I'd use that to encrypt my message, and the private key would never have to be shared in a public space. This is _undoubtedly_ more secure than symmetric encryption.

### Result
Tasks:
-	Generate a key pair.
    -	RSA private key:
-----BEGIN RSA PRIVATE KEY-----
MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAJ4vFENmT2KgpYVKcbhqGWUyOX7yCPNLiMT+je/YGWtR09zaO3FV/GiPIzYijpUyDGx98Od+lSm/Vrx25wEjQCscIj/GgyKDqbXPPV0NunntjnBHHOGceEwRvQouDYx/VYHtm6+1JrCdJM8oEDmafr78Q4V+jrRL3j938nPV2pSnAgMBAAECgYBvlfhuX0LK6VY6A7zbAYVunJJwmZ50uij+Bi/sLH4p9axFlHDwT17iB28oZhI87vRSqDkDpIjmzUILarkkVVCSvH4WOt8jsmcg5oX5e+v//IHFfizYUukSskijXXinvMuqtGbuYT6XCr0SoRThDXn6WjmFsyPm1NpgwiI+yO6lUQJBANGGkss+vGWzzGR3Si/VmYkxFR9rIPcgu5bv1yFBKN2wCCk5a1x6J6p2npxhLkYdryLpFI3FMc/838JBTS7gYM8CQQDBRS7Sq55c8EMPAL+Aa33RW93TwDl8DYxJMKc600KMZxPNBjQFaHkahukmpTbwtg0QBlskQ964zq0acIp6zZSpAkEAvX1daN6V98yBvyJ7P4OH1aFEHyP9rkI2JS1HfFW3pbY7yzyYsgvvr6STkY36EYNrDsGIyyZaBGYH32C7cveN1QJAYXlf9RZjJ2Jxn7Zz3vPXn+hiR3KSS3OVxjAIl42G6cLu5J91Syj2sx9JpZj7zYkzq1pZS0ADq1dpTIVoAil/CQJAZUZ0UC5zWxuSIhIeeuqttQmzUchZBpvKh2EDfEGmi4nyhkOdEcAfrX5DBdBVLz1upudZfYtqd5aNZ+gEQ0ri1g==
-----END RSA PRIVATE KEY-----

    -	Public key:
-----BEGIN PUBLIC KEY-----
MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeLxRDZk9ioKWFSnG4ahllMjl+8gjzS4jE/o3v2BlrUdPc2jtxVfxojyM2Io6VMgxsffDnfpUpv1a8ducBI0ArHCI/xoMig6m1zz1dDbp57Y5wRxzhnHhMEb0KLg2Mf1WB7ZuvtSawnSTPKBA5mn6+/EOFfo60S94/d/Jz1dqUpwIDAQAB
-----END PUBLIC KEY-----

-	Send an asymmetrically encrypted message to one of your peers via the public Slack channel. They should be able to decrypt the message using a key. The recipient should be able to read the message, but it should remain a secret to everyone else. You are not allowed to use any private messages or other communication channels besides the public Slack channel. Analyse the difference between this method and symmetric encryption.
    -	The message was a success. I encrypted a message with Elmarie's public key. She was then able to decrypt the message with her private key.
    -	The difference between symmetrical and asymmetrical encryption is quite big. They both require a key to be shared in public, but the way in which they do so differs immensely. You don’t need to obfuscate the public key with asymmetrical encryption, which increases ease of use quite a bit. The private key can stay hidden, which is a big safety plus. I don’t quite understand how the public key can be found in a directory, although perhaps it’s as easy as looking up someone’s name. This means only one party is needed (after the initial creation of a public key) to create the encrypted message, and no effort is needed by the receiving party to decode the key used in symmetrical encryption. Quite a bit more efficient. 

