# [OSI Stack]
OSI model

Got some troubleshooting to do with your telecommunication or computing systems? The Open Systems Interconnection (OSI) model is here to help. This is what it’s primarily used for. 
With 7 layers, each represents a different part of network communications. Each layer has different protocols that it uses. 

Taking a top-down or bottom-up approach is a good way to use the OSI model for troubleshooting. Going through all layers until the problem has been identified. 

There is also, as an alternative to the OSI model, the TCP/IP model. This model describes the standard on which the internet was built. This makes it a more realistic model, but OSI is generally a more practical model for troubleshooting. Because of its extra layers. 


## Key-terms
OSI model: A model that has 7 layers, each representing a different part of network communications. 

TCP/IP model: A model that has 4 layers. Similar to the OSI model, but less practical when troubleshooting. This is because the OSI model has more layers.

## Assignment
### Used sources
[Source 1: OSI model](https://www.dummies.com/article/technology/information-technology/networking/general-networking/layers-in-the-osi-model-of-a-computer-network-168519/)

[Source 2: TCP/IP model](https://www.dummies.com/article/technology/information-technology/networking/general-networking/network-basics-tcpip-protocol-suite-185407/)

### Experienced problems
I'm running into the problem of time management. It's difficult for me to determine where to cut off my learning in favour of getting on with the assignments. I think this problem will solve itself when I'm all done with moving houses, as I can then focus completely on the course. I like to take my time with things so I can process everything in a relaxed manner.

### Result
* The OSI model and its uses:

    1.	**The Physical Layer:**  

        This is the bottom layer. Specified in it are the physical characteristics of the network. Think of cable type used, connectors used, length of cable, etc. e.g. the Ethernet standard for 100BaseT cable specifies the electrical characteristics of the twisted-pair cables, the size and shape of the connectors, the maximum length of the cable, etc.  

    2.	**The Data Link Layer:**  
    
        This is the lowest layer where meaning is assigned to the transmitted bits over the network. Things like addressing each packet so it arrives at the intended recipient, addressing the size of each data packet to be sent, making sure that two or more nodes don’t try to transmit data on the network at the same time. 
        Basic error detection and correction also happens on this layer. This makes sure that the same data sent is the data received. 
        On this layer each device has a MAC (Media Access Control) address. In the factory where a device is made, it gets its MAC address. It is the hardware address.  

    3.	**The Network Layer:**  

        This is where network messages from one computer to another are routed. Each device is given a logical address (with for instance an IP or IPX protocol) to do so.
        Routing also happens when a computer on one network needs to send a packet to a computer on another network. For this, the aptly named ‘router’ is used.  

    4.	**The Transport Layer:** 

        Here we find the basic layer where one network computer communicates with another network computer. One of the most popular networking protocols: TCP (Transmission Control Protocol) is found. The Transport Layer’s main purpose is to make sure that packets surf the local network without any errors.  

    5.	**The Session Layer:**  

        You might have guessed it… this is where sessions (instances of communication and data exchange) between network nodes are established. Before any data can be transmitted over the network, a session must be established. The Session Layer keeps these sessions running real smooth like.  

    6.	**The Presentation Layer:**  

        What we see on this layer is the conversion of data sent over the network from one type of representation to the next. Sophisticated compression techniques can be applied before send off, and undone at the other end of the transmission.
        on the Presentation Layer, data can also be scrambled before, and unscrambled after transmission. Fancy schmancy encryption techniques are used for this.    

    7.	**The Application Layer:**  

        The highest layer of the OSI model, the Application Layer. This layer deals with techniques that application programs use to communicate with the network. Application programs themselves don’t come into play on this layer, rather how they interact with the network. HTTP (HyperText Transfer Protocol) is a good example of an Application Layer protocol.  


  
* The TCP/IP model and its uses:  
    -   **TCP/IP model:**

        The TCP/IP (Transmission Control Protocol/Internet Protocol) is the protocol on which the internet is built. Despite its name, it consists of an entire suite of related protocols. 
        It is based on a four-layer model of networking that is similar to the seven-layer open systems interconnection (OSI) model. 

    -   **IP:**  

        A network layer protocol responsible for delivering packets to network devices. IP is a routable protocol, this means packets can be forwarded from one network to another.

