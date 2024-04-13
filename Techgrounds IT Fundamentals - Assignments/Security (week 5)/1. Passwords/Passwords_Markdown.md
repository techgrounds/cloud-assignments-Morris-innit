# [Passwords]
Previously, we've talked about the three factors of authentication. Passwords fall into the 'something you know' category. Passwords can be guessed on the front-end. To make this harder we can use the following strategies:

-   No common passwords
-   Long passwords
-   Use of special characters like #,*,+,!, etc.
-   Mix up those CAPITAL and small letters
-   No birthdates, pet names, or other easily deducible passwords
-   Unique password for each login
-   Use of passphrase

Because remembering passwords becomes a right drag with all these strategies, password managers were created. On the back-end, passwords need to be stored securely. This is done by storing them hashed. Now, if your database (or /etc/shadow file in Linux) gets leaked or stolen, hackers don't have a plaintext of your passwords. Hackers try to use a Rainbow Table to crack hashed passwords.
 
## Key-terms
Hashing: A one-way encryption algorithm used to encrypt different kinds of data. One-way means that there is no key used in the process to make decryption possible.

Checksum: A hashing algorithm used to validate the integrity of files of programs to ensure your download hasn't been tampered with.

Rainbow Table: A tool used to decrypt hashes. This is possible when hashes are leaked. The algorithm is then figured out and turned into a Rainbow Table that can decipher hashes.

## Assignment
### Used sources
[Source 1: What is hashing?](https://builtin.com/articles/what-is-hashing)

[Source 2: Applications of hashing](https://www.geeksforgeeks.org/applications-of-hashing/)

[Source 3: What is a Rainbow Table?](https://www.beyondidentity.com/glossary/rainbow-table-attack)



### Experienced problems


### Result
Tasks:

-	Find out what hashing is and why it is preferred over symmetric encryption for storing passwords.
    -	Hashing is the process of applying a hashing algorithm to a certain piece of information, be it a piece of plaintext, file, or program, or another type of data. This is done for a multitude of reasons, e.g. database indexing, password storage, data compression, all the way to fraud detection. 
    -	Hashing is preferred for storing passwords over symmetric encryption because there is no key offered with the encryption. This makes it an irreversible action, and thus harder for hackers to get anything valuable out of the hashes.   
    
-	Find out how a Rainbow Table can be used to crack hashed passwords.
    -	When hashes are leaked, a Rainbow Table can be made to decipher the hashing algorithm. This Rainbow Table then makes it very easy to decrypt any data that has been encrypted with said hashing algorithm.
    -	Below are two MD5 password hashes. One is a weak password, the other is a string of 16 randomly generated characters. Try to look up both hashes in a Rainbow Table.  

            03F6D7D1D9AAE7160C05F71CE485AD31	 	Result is: ‘welldone!’  

            03D086C9B98F90D628F2D1BD84CFA6CA		Result: Unable to crack, so the result was ‘Not found.’	

-	Create a new user in Linux with the password 12345. Look up the hash in a Rainbow Table.
    -	I did this with the following commands:
        -	```sudo useradd user1```
        -	```sudo passwd user1```
        -	```cat /etc/shadow```
    -	The hash: $6$M4ArJDmkUYKZd5zi$rCsls/VCM9dYCJSOathSO6Z5MkU4QFQURsA6gHe94FF9vz3U.QVVPT5l7M4R5Ol/OAn/3sYXgXTH/WyWTY5Q41:19821:0:99999:7:::
    -	Result of cracking: ‘Unrecognised hash format.’
-	Despite the bad password, and the fact that Linux uses common hashing algorithms, you won’t get a match in the Rainbow Table. This is because the password is salted. To understand how salting works, find a peer who has the same password in /etc/shadow, and compare hashes.
    - When comparing the hashes, the sizes weren't alike. What was alike, however, was the beginning and end part of the hash. "$6$", and ":19821:0:99999:7:::" respectively. 

