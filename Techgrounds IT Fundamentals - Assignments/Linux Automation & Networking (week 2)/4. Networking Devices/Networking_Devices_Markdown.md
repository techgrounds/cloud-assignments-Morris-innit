# [SNetworking Devices]
Want to connect more than two computers? You're going to need a network with network equipment. To list some of the equipment:

- router
- switch
- repeaters
- access point

Each one of the listed pieces of equipment contributes to your data being sent to the right computer. Smart as they are, they can communicate between themselves so that you as a user don't need to worry about any settings. Add to, or remove a computer from the network? No worries, they know what to do. Protocols play an important roll in this. 

There exist different variations of a switch that work on different layers of the OSI-model. Because of this, implementations of network equipment can matter.

AWS and Azure offer services that do the same thing as network equipment does. Each network concept (routing, gateways, switching) has one or more cloud equivalents. 

## Key-terms
Router: a device that forwards data packets to the appropraite parts of a computer nerwork.

Switch: a device that connects devices in a network to each other so that they can talk by exchanging data packets.

Repeaters: a device that amplifies incoming signals and sends them over a wider area or higher network layer than the original signal.

Access point: a device that allows other Wi-Fi devices to connect to a wired network or wireless network. It acts as a standalone root unit and serves as the focal point for communications, so as to increase the communication range of wireless users. 

## Assignment
### Used sources
[Source 1: Router - Data packet routing](https://aws.amazon.com/what-is/routing/#:~:text=manage%20traffic%20volume.-,How%20does%20routing%20work%3F,might%20route%20it%20multiple%20times.)

[Source 2: Router - Network address filtering](https://www.ibm.com/docs/en/i/7.4?topic=security-ip-filtering-network-address-translation)

[Source 3: Router - Acting as an intermediary between networks](https://www.avg.com/en/signal/what-is-a-router)

[Source 4: Switch - Functions of a switch](https://www.linkedin.com/pulse/functions-switch-evelyn-shi/)

[Source 5: Switch - Physical addressing](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)

[Source 6: Switch - Network topology](https://networklessons.com/cisco/ccna-routing-switching-icnd1-100-105/network-topologies)

[Source 7: Switch - Error checking](https://etutorials.org/Networking/lan+switching/Chapter+6.+How+a+Switch+Works/Layer+2+Switching+Methods/)

[Source 8: Switch - Frame sequencing](https://www.ibm.com/docs/en/i/7.3?topic=support-ethernet-frame-format)

[Source 9: Switch - Flow control](https://en.wikipedia.org/wiki/Flow_control_(data))

[Source 10: Repeater - Functions of a repeater](https://nordvpn.com/nl/cybersecurity/glossary/repeater/#:~:text=Repeater%20is%20a%20type%20of,provide%20access%20to%20inaccessible%20nodes.)

[Source 11: Repeater - Increase network range](https://www.screenbeam.com/wifihelp/wifibooster/differences-wifi-booster-wifi-extender-wifi-repeater/#:~:text=As%20the%20name%20implies%2C%20wireless,response%20time%2C%20is%20typically%20increased.)

[Source 12: Repeater - Restore damaged or weak signal & Provide access to inaccessible nodes](https://www.rfpage.com/wi-fi-repeaters-how-it-works/)

### Experienced problems
When looking up what a repeater does I came across a few sources that seemed to contradict each other. Some saying it extends the range of a wifi signal, but using the quality that it receives, and others saying it actually amplifies the signal. My understanding of it is that it does amplify it in the sense that it increases the range, but it does not amplify it by increasing the strength of the signal that it receives. The terminology threw me off a bit. 



### Result
Tasks:
*	List and describe the functions of common network equipment.
    -	**Router:** 
        -	**Data packet routing:** sending data packets across a network towards their intended destination. A router looks up the data packet address that is found in a routing table. This information comes from a header that each data packet holds.
        -	**Network address filtering:** this process lets you control the IP traffic that will be allowed to go in and out of your network. With defined rules it filters out packets and protects your network.
        -	**Acting as an intermediary between networks:** using the IP (internet protocol) system, routers send data to the right IP address, and manage internet traffic.

    -	**Switch:** a device that connects devices in a network to each other so that they can talk by exchanging data packets.
        -	**Physical addressing:** by way of MAC addresses, switches send data packets to a single intended device, unlike a router that sends data packets across network paths to reach their destination.
        -	**Network topology:** this is the way in which devices are connected to, and communicate with each other. 
        - 	**Error checking:** with the CRC (Cyclic Redundancy Check) method, the switch uses a mathematical formula, based on the number of bits (1s) in the frame, to determine if an error occurred in the received frame.
        -	**Frame sequence and flow control:** FCS (Frame Check Sequencing) verifies each frames information is not damaged during transmission. When frames are corrupted, the FCS frame will not match the receiver’s calculated FCS. When this happens the corrupted frames will be discarded.   
        Flow control manages the rate of data transmission between to nodes. This prevents a faster sender overwhelming a slow receiver. 

    -	**Repeaters:** a device that amplifies incoming signals and sends them over a wider area or higher network layer than the original signal.
        -	**Increase network range:** by re-broadcasting the Wi-Fi signal to a finite localised area, the signal is able to reach further than it would without the repeater. Signal strength is not increased, but latency typically is.
        -	**Restore damaged or weak signal:** by gathering and broadcasting the Wi-Fi signal at an increased power, the damaged or weak signal will restore it’s health, so to speak.
        -	**Provide access to inaccessible nodes:** this increase of power extends the range of the Wi-Fi signal, and previously inaccessible nodes will now fall into reach of the WiFi network. 

    -	**Access point:** a device that allows other Wi-Fi devices to connect to a wired network or wireless network. It acts as a standalone root unit and serves as the focal point for communications, so as to increase the communication range of wireless users.
        -	**Allow wireless-capable devices to connect to a wired network:** basically it does what a switch does, but then wirelessly. 


-	Most routers have an overview of all connected devices, find this list. What other information does the router have about connected devices?
    -	It sees your IP address, MAC address, device name, and the kind of device.

-   Where is the DHCP server on your network? What are its configurations? (Done with the help of a classmate because of a shared network at home)
    -	It can be found in the settings:
        -	DHCP server		: on
        -	LAN IP address		: 192.168.2.254
        -	Subnet mask		: 255.255.255.0
        -	DHCP start IP address	: 192.168.2.1
        -	DHCP end IP address 	: 192.168.2.200
        -	ISP DNS		: Off		
        -	Primary DNS		: 192.168.2.254
        -	Lease time		: 86400

