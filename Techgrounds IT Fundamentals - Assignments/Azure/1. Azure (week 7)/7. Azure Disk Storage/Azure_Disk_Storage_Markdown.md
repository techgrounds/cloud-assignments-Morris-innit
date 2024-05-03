# [Azure Disk Storage]
Azure Disk Storage is like a virtual hard drive on the cloud. A disk can be an OS Disk (this holds the OS) or a Data Disk (comparable to an external hard drive). You have a choice between a Managed Disk amd an Unmanaged Disk. Unmanaged Disks are cheaper, but you'll need a Storage Account (you'll also need to manage the disk yourself). Managed Data Disks can be shared by multiple VM's, but it's a relatively new feature, and it has some catches. Backups of a Managed Disk can be made with Incremental Snapshots that only save adjustments made since the last snapshot. For an Unmanaged Disk you can only make "normal" snapshots. There are 5 Managed Disk types. In gerenal it can be said that more performance creates higher costs. See https://learn.microsoft.com/en-us/azure/virtual-machines/disks-types for an up-to-date overview of the available disk types. 

A disk can be encrypted for security. Disks can also be made larger, but not smaller. If you want to use an external device (including a Data Disk) with Linux, you'll have to mount it first.

## Key-terms
[Schrijf hier een lijst met belangrijke termen met eventueel een korte uitleg.]

## Assignment
### Used sources
[Plaats hier de bronnen die je hebt gebruikt.]

### Experienced problems
I didn't quite understand how to locate the correct directory for my shared disk. Since its location started with ```/dev/```, and I couldn't find that directory explicitly named. Some extra questions in the ol' Chat GPT cleared things up. 
I also had to create a file system on the shared disk before being able to mount it.

### Result
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]
