# [IP Addressing]
For network devices to find each other on the network, IP addresses are used. IP addresses are logical addresses that can be assigned to a network device. An IPv4 address has 32 bits (4 bytes). It is mostly written in decimals e.g. 132.88.142.5. Each of the 4 numbers, separated by a period, represents 1 byte. Since one byte has a maximal value of 255, each of the 4 numbers can also have a maximum value of 255.

With 4,294,967,296 total possible IPv4 addresses, all usable IPv4 addresses have been either sold or reserved by now. 

The original idea was that each computer would be communicated with through their own IPv4 address. This idea has been long abandoned. 

Measures have been taken to prolong the use of IPv4. For instance, each device on a network shares one public IP address. The NAT-table in your modem makes this possible. A NAT-table keeps track of the connections that all of the devices on a private network have with the public internet. It then assures that the data coming into the network arrives at the right device.

3 IP address ranges are reserved for private networks:

- 192.168.0.0 - 192.168.255.255
-  172.16.0.0 - 172.31.255.255
-   10.0.0.0 - 10.255.255.255

IPv6 addresses are the successors of IPv4 addresses. IPv6 addresses contain 128 bits, and is often notated as a hexadecimal number. Because of this, the total number of IPv6 addresses is so big it is said that each grain of sand on all beaches on earth could be given 3 IPv6 addresses.

As of right now, AWS and Azure still mainly use IPv4 addresses, even though the transition to IPv6 is inevitable. 

## Key-terms
IP (Internet Protocol) address: An address used to communicate between websites and devices. It's how information you're looking for finds you.

IPv4 (Internet Protocol version 4): A protocol using 4 bytes to create IP addresses.

IPv6 (Internet Protocol version 6): A protocol using 16 bytes to create IP addresses. Commonly notated using a hex (hexadecimal) number.  
Why not IPv5, I hear you ask? There actually was an IPv5, intended as a streaming protocol, but it died as a draft. 

Public IP address: an address assigned to your router by your ISP (Internet Service Provider), to communicate with the internet. This address is public to the whole internet

Private IP address: an address given to each device in a network by the router, so that they can all communicate with each other internally. This address is public only to the other devices within a network.

NAT (Network Address Translation): is used as an intermediary between the the public IP, and private IP('s). When information is sent to a network's public IP, it is processed by NAT and sent to the right private IP. This way a private IP can remain private. Instructions can also be given to keep information out. You can see it as a receptionist at the frontdesk of an office.

Static address: A static address is an address that doesn't change. It is set either by your ISP, or manually.

Dynamic address: A dynamic address is an address that does change. The DHCP (Dynamic Host Configuration Protocol) assigns these addresses.

## Assignment
### Used sources
[Source 1: Where is IPv5?](https://www.cloudns.net/blog/ipv4-vs-ipv6-internet-protocol/#:~:text=The%20reason%20is%20that%20IPv5,eventually%20died%20as%20a%20draft.)

[Source 2: Public and private IP address explained](https://www.avast.com/c-ip-address-public-vs-private)

[Source 3: What is NAT?](https://avinetworks.com/glossary/network-address-translation/#:~:text=Network%20Address%20Translation%20(NAT)%20is,private%20network%20a%20public%20address.)

[Source 4: Static & Dynamic IP addresses](https://www.security.org/vpn/static-vs-dynamic-ip-address/)

[Source 5: What happens when you change the private IP address of one host to that of another host on the same network? Answered by Chat GPT](https://chat.openai.com/c/8d150b5d-9b2d-4779-9fad-ffdb7bdab719)

### Experienced problems


### Result

I’m not able to go into my router, so all answers given are done through sources online.  

-	Find out what your public IP address is of your laptop and mobile on wifi.  
    -  Are the addresses the same or not? Explain why.  
        -   The addresses are the same. This is because each network shares one public IP address.  

-	Find out what your private IP address is of your laptop and phone on wifi.  
    -	Are the addresses the same or not? Explain why.
        -   These addresses are not the same. This is because private addresses are created to distinguish devices within a network without having to use multiple public IP addresses.   

-	Change the private IP address of your phone to that of your laptop. What happens?
    -   The long answer can be found in source 5. The short answer is that both hosts will probably experience connectivity issues because of an IP address conflict.  

-	Try to change the IP address of your phone to an address outside of your network. What happens?
    -   The host will simply not be able to connect to the network. 


