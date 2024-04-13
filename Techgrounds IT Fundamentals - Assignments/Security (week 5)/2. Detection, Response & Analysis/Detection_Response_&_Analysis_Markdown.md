# [Detection, Response & Analysis]
Try as you might, some attacks will slip through your prevention systems. Social engineering is the most common method of getting malicious software (malware) into a network. Got hit with an attack? The three steps to follow are: Detection, response, and analysis. 

The first step to stopping those pesky hackers is detecting an (attempted) attack. Tools like Wireshark, that can analyse a network to detect anomalies, can be helpful here. Intrusion detection systems (IDS) and intrusion prevention systems (IPS) are also used for this purpose. 

Has an attack been detected? Then the first step is to try and contain the damage. The way you do this depends on the kind of attack. After containing the attack, you can try figuring out the root cause of the attack, to then be able to stop it. Finally, you enter the recovery phase, where you try and get all systems back online, and you assess the done damages. 

Having a response plan in place for when an attack happens is **vitally** important.

In the analysis phase, all that you've learned will be documented. You then harden your systems to prevent a similar attack from happening. Sometimes an OS update is all that it takes. 

Response and analysis are part of a disaster recovery plan. In a bigger business continuity plan, this plan cannot be overlooked. A business could be done for if infrastructure goes offline after a disaster strikes. Having a cold backup, or a redundant site, are two of the many strategies you could implement in a disaster recovery plan.

With these strategies, it's always important to keep track of the following metrics: How much data is lost on incident (Recovery Point Objective; RPO), how long it takes to be back online (Recovery Time Objective; RTO), and cost.

## Key-terms
Malware (Malicious Software): Malware is an umbrella term used to describe any malicious program or code that is harmful to a system. 

IDS (Intrusion Detection Systems): A network security tool to monitor network traffic and devices known for malicious activity, suspicious activity, or security policy violations.

IPS (Intrusion Prevention Systems): An intrusion prevention System does the same as an IDS, but also blocks threats. It does this by alerting the security team, terminating dangerous connections, removing malicious content, or triggering other security devices.

RPO (Recovery Point Objective): The recovery point objective is the maximum amount of data - measured by time - that can be lost after a recovery from either a failure, disaster, or other comparable event before data loss will surpass an organisation's acceptable limit. 

RTO (Recovery Time Objective): The recovery time objective is the maximum amount of time that a network, application, system, or computer can be down after an unexpected failure, disaster, or other comparable event takes place.

## Assignment
### Used sources
[Source 1: What is an IDS?](https://www.ibm.com/topics/intrusion-detection-system)

[Source 2: What is an IPS?](https://www.ibm.com/topics/intrusion-prevention-system)

[Source 3: What is an RPO?](https://www.druva.com/glossary/what-is-a-recovery-point-objective-definition-and-related-faqs#:~:text=Recovery%20point%20objective%20definition&text=Recovery%20point%20objective%20(RPO)%20is,is%20acceptable%20to%20an%20organization.)

[Source 4: What is an RTO?](https://www.druva.com/glossary/what-is-recovery-time-objective-definitions-and-related-faqs#:~:text=Recovery%20time%20objective%20definition&text=The%20recovery%20time%20objective%20(RTO,or%20comparable%20event%20takes%20place.))

[Source 5: Hack response strategies](https://www.apptega.com/blog/5-tips-for-responding-to-cyber-attacks)

[Source 6: What is systems hardening?](https://www.beyondtrust.com/resources/glossary/systems-hardening)

[Source 7: Types of disaster recovery sites](https://blog.icorps.com/bid/101789/types-of-disaster-recovery-sites)

[Source 8: What is malware?](https://www.malwarebytes.com/malware)

### Experienced problems


### Result
**Tasks:**

**Study:**
-	IDS and IPS.
    -	Check key terms.
-	Hack response strategies.
    -	Here are 5 hack response strategies:
        1.	Follow a communication plan.  
        It is critical to figure out who to inform after a hacking attack. What does the attack mean? Who should you tell? How do you tell them? When do you tell them? You should implement a communication plan before the hacking attack occurs so you can carry it out once the attack takes place.  
        2.	Secure IT systems.  
        Right as you realise the breach, secure your IT systems so that you limit the scope of the attack.  
        3.	Launch backups.  
        Just like the communication plan, it is critical to have a good crash plan developed for your website. Now is the time to launch that crash plan and deploy your backups to protect your data from any further harm.
        4.	Notify authorities.  
        Contact the authorities about the cyber attack on your organisation. This helps to protect your customers and makes a record of the attack so that authorities can respond.
        5.	Create redundancy in your data.  
Another critical part of data security and protecting your assets. Data redundancy is a condition created within a database or data storage technology where the same piece of data is held in two separate places.   
-	The concept of systems hardening.
    -	Systems hardening is a collection of tools, techniques, and best practices that aim to reduce vulnerability in technology applications, infrastructure, systems, firmware, and other areas. This practice reduces security risk by eliminating potential attack vectors and condenses the system’s attack surface.   

-	Different types of disaster recovery options.  
    1.	Cold Computing Sites:  
    This is the most basic type of disaster recovery site. It consists of elements providing power, networking capabilities, and cooling.
    2.	Warm Computing Sites:  
    Has all elements of a cold computing site with additional elements: storage hardware such as tape or disk drives, servers, and switches.
    3.	Hot Computing Sites:  
    A fully functional backup site that has important data mirrored in it.   

**Exercise:**
-	A Company makes daily backups of their database. The database is automatically recovered when a failure happens using the most recent available backup. The recovery happens on a different physical machine than the original database, and the entire process takes about 15 minutes. What is the RPO of the database?
    -	24 hours and 15 minutes.
-	An automatic failover to a backup web server has been configured for a website. Because the backup has to be powered on first and has to pull the newest version of the website from GitHub, the process takes about 8 minutes. What is the RTO of the website?
    -	8 minutes.
