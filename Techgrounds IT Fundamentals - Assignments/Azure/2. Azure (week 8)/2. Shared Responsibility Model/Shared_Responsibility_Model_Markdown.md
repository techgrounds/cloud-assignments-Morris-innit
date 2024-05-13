# [Shared Responsibility Model]
When you're running your own datacentre, you can be sure that you're responsible for everything: from the physical security to the security and encryption of your data. Not to mention the maintenance and management of the building where you have your datacentre, and all the personnel that's needed for that.  
In the Cloud a lot of these responsibilities are taken over. The Cloud Provider is responsible for the physical side of your infrastructure. You as a customer can rent this infrastructure without having to worry about it. 

This is no absolvement of responsibility, however. You as the customer are still responsible for what you do on this rented infrastructure. These are things that go from access control to data and software, encryption of data at rest and data in transit. 

How much responsibility is the customer side also depends on what services are being used. Still, there remain responsibilities that will always be for the customer.

![SRM](shared-responsibility.svg)

The Cloud provider offers extra services with which you can more easily manage your responsibilities. 

## Key-terms


## Assignment
### Used sources
[Source 1: Shared Responsibility Model](https://learn.microsoft.com/en-us/azure/security/fundamentals/shared-responsibility)

### Experienced problems
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Result
**Study:**
-   The Azure Shared Responsibility Model
    -	As is neatly shown in the image above, when you work in the cloud your responsibilities diminish. When you have an on-premises datacenter, all the responsibility falls on you. Going down the ladder from Infrastructure as a Service (IaaS), to Platform as a Service (PaaS), to Software as a Service (SaaS), your responsibilities diminish and fall into the hands of the Cloud Provider. There will always be a number of responsibilities for you as the customer, and they’re the following: 
        -	Data
        -	Endpoints
        -	Account
        -	Access management
