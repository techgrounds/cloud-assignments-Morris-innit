# [IAM]
There are two steps in security: authentication & authorisation. Whenever you log in, both happen as two different actions. A common way to improve security is multi-factor authentication (MFA).

Best practice is to follow the principle of least privilege for authentication.

## Key-terms
Authentication: When a user of computer has to prove its identity to the client or server. This can be done in a couple of ways, the most common being a username and password. A pin code for your card is another way, as are fingerprints, etc.

Authorisation: When a server determines if the client has permission to access a file it is called the authorisation process. Authentication can be used for this, since then the server knows who is requesting access, and if access is granted to that person or computer.

Multi-factor authentication: The process of using multiple factors for authentication. Think a password combined with a fingerprint, or a password combined with a smart card.



## Assignment
### Used sources
[Source 1: What are authentication & authorisation?](https://www.bu.edu/tech/about/security-resources/bestpractice/auth/#:~:text=Authorization%20is%20a%20process%20by,is%20that%20is%20requesting%20access.)

[Source 2: What is three factor authentication?](https://www.pearsonitcertification.com/articles/article.aspx?p=1718488)

[Source 3: What is the principle of least privilege?](https://www.paloaltonetworks.com/cyberpedia/what-is-the-principle-of-least-privilege)

### Experienced problems

### Result
Tasks:

-	The difference between authentication and authorization.
    -   Authentication is done by proving the identity to the client or server, usually by way of a username and password. Authorisation is the process of determining if said user has access to certain files or resources. These two processes are usually done together.
-	The three factors of authentication and how MFA improves security.
The three factors of authentication are:
    1.	Something you know (password or key phrase)
    2.	Something you have (smart card or token)
    3.	Something you are (biometric method)  

    -   MFA (Multi-Factor Authentication) improves security by building on top of each other. By combining multiple factors of authentication you decrease the chance of a malicious player cracking the security. For instance, someone might have gotten access to your password or key phrase. If a smart card or token are also needed for authentication, this person still cannot enter. The most difficult to crack being your biometrics. Sadly the biometric factor is also susceptible to false reject or false accept errors.
-	What the principle of least privilege is and how it improves security.  

    -   The principle of least privilege is where you limit the access of a user to only the specific data, resources, and applications they need to complete their required tasks. This way there will be less risk of potential breaches and misuse of data and critical systems. The attack surface is limited, and human error is minimised.  
    It is a fundamental pillar of zero trust network access (ZTNA) 2.0.

