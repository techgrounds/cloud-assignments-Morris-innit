# [Protocols]
[Geef een korte beschrijving van het onderwerp]

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Assignment
### Used sources
[Source 1: Meaning of Seq (Sequence) in Wireshark](https://www.ibm.com/docs/en/zos-basic-skills?topic=4-transmission-control-protocol-tcp)

[Source 2: Meaning of Ack (Acknowledgement) in Wireshark](https://en.wikipedia.org/wiki/Acknowledgement_(data_networks)#:~:text=In%20data%20networking%2C%20telecommunications%2C%20and,part%20of%20a%20communications%20protocol.)

[Source 3: Meaning of Len (Length) in Wireshark](https://networkengineering.stackexchange.com/questions/7480/tcp-length-and-tcp-data-wireshark-filters#:~:text=Simply%20put%2C%20tcp.,within%20the%20TCP%20segment%20data.)

[Source 4: Chat GPT to figure out the second task](https://chat.openai.com/)

### Experienced problems
The only problem I experienced was having to catch up to assignments still. I feel it is making me scatterbrained and inefficient in my approach.

### Result
Tasks:
*	Identify several other protocols and their associated OSI layer. Name at least one for each layer.
    -   **The Physical Layer:** Bluetooth
    -   **The Data Link Layer:** MAC (Media Access Control)
    -   **The Network Layer:** IPv4/IPv6 (Internet Protocol)
    -   **The Transport Layer:** TCP (Transport Layer Protocol)
    -   **The Session Layer:** ZIP (Zone Information Protocol)
    -   **The Presentation Layer:** JPEG (Joint Photographic Experts Group)
    -   **The Application Layer:** HTTP (Hypertext Transfer Protocol)
*	Figure out who determines what protocols we use and what is needed to introduce your own protocol.
    -   There are industry standards bodies, like the IETF (Internet Engineering Task Force). Government regulations may also be of influence. Just like market forces and technological advancements. 
    -   To introduce your own protocol you need to do quite some stuff. You need to design and develop it, prototype and test it, then standardise it, to then finally deploy it and try to reach adoption.
*	Look into wireshark and install this program. Try and capture a bit of your own network data. Search for a protocol you know and try to understand how it functions.
    -   Through the TCP (Transmission Control Protocol) I can see packets of data being sent from one IP to another, back and forth. This is being done through IPv4 (Internet Protocol version 4). I can see the Src (source) port number (80) and Dst (destination) port number (63376). I can also see the Seq (sequence) packet size (371221 B), the Ack (acknowledgement) packet size (140 B), and the Len (length) packet size (1380 B).

