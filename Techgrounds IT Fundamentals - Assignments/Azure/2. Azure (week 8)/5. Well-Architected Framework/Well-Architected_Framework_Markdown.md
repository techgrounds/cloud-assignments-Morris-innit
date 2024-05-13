# [Well Architected Framework]
Cloud Providers benefit that their customers have good, secure applications running on the infrastructure of the provider. To give customers a guideline on what good, secure applications look like, the Well-Architected Framework has been called to life. The Well-Architected Framework of Azure and AWS look very similar. They are based on almost the same 'pillars,' namely:  

-   Reliability
-   Security
-   Cost Optimisation
-   Operational Excellence
-   Performance Efficiency

A mnemonic device to remember these pillars is CROPS.  
Each pillar delves into an aspect of your application, and how the Cloud can help optimise it.  

As a cloud engineer it is important to be able to build an application with this Well-Architected Framework that optimally uses the possibilities of the Cloud.

## Key-terms


## Assignment
### Used sources
[Source 1: The Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/what-is-well-architected-framework)

[Source 2: The Design principles](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html)

### Experienced problems


### Result
**Study:**
-	**Well-Architected Framework of Azure**
    -	There are 3 layers to the Well-Architected Framework of Azure:
        -	Pillars:  

            The foundation of this framework lies in the pillars. If you don't have a comprehensive understanding of these pillars, the subsequent layers—the workload layer and service guides—might not be fully comprehensible.
            We’ll delve into that a little deeper down below.
        -	Workload:  

            The workload layer represents how the pillars apply to a specific class of workload. During the initial design phase, workload architecture is segmented based on utility, and each segment represents the prioritized or design areas. These design areas are specific to the workload class and serve as focal points for optimization. The Well-Architected Framework includes several workloads. Find one that closely matches your business requirements.

            Begin with Get started to understand the solution context. As a refresher, read the Design principles to understand how the workload adopts the pillar guidance. Then, dive deep into Design areas that focus on the technical decision points with recommendations that follow. Workload guidance also includes an assessment that helps you evaluate your readiness in production.

            For more information, see [About the Well-Architected Framework workloads.](https://learn.microsoft.com/en-us/azure/well-architected/workloads)
        -	Service guides:   

            Service guides are instrumental in decision-making related to the individual Azure components that reside within the workload. They offer the core features and capabilities of each service that are necessary to attain architectural excellence. It’s important to note that these guides aren’t configuration guides. Also, they aren’t a compiled list of all features and capabilities. The intent is to highlight the utility of the features through Well-Architected pillar perspectives.

        For more information, see the [available guides.](https://learn.microsoft.com/en-us/azure/well-architected/service-guides/)
-	**How each pillar can be implemented into cloud-services**
    -	Cost Optimisation
        -	Optimising on usage and rate utilisation while keeping a cost-efficient mindset. [Design principles](https://learn.microsoft.com/en-us/azure/well-architected/cost-optimization/principles)
    -	Reliability
        -	Design for business requirements, resilience, recovery, and operations, while keeping it simple. [Design principles](https://learn.microsoft.com/en-us/azure/well-architected/reliability/principles)
    -	Operational Excellence 
        -	Streamline operations with standards, comprehensive monitoring, and safe deployment practices. [Design principles](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/principles)
    -	Performance Efficiency 
        -	Scale horizontally, test early and often, and monitor the health of the solution. [Design principles](https://learn.microsoft.com/en-us/azure/well-architected/performance-efficiency/principles)
    -	Security
        -	Protect confidentiality, integrity, and availability. [Design principles](https://learn.microsoft.com/en-us/azure/well-architected/security/principles)

          
    For more information, see [About the Well-Architected Framework pillars.](https://learn.microsoft.com/en-us/azure/well-architected/pillars)
