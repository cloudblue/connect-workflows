# Price List Versions
## Overview
The CloudBlue Connect platform allows establishing and automating the cost-effective process of the price lists exchange from Vendors to Distributors or Resellers. Price lists versions, as the name implies, represent versions of a particular price list object. Versions include various values associated with items for each attribute of the price list. Therefore, price list objects can be considered as *templates* for their corresponding versions. Note that price list versions are created and managed via the Pricing module on the CloudBlue Connect platform.  

In general, new versions can be generated for your existing price list objects in any state. A single price list can have several versions within the system. Therefore, the system prompts to select your base price list version before creating a new version object. Version objects can be removed in case they are assigned to the *Draft* state.  

Once a version object is activated, the system automatically activates its corresponding price list object. The system allows scheduling and unscheduling the version activation. The system also allows activating such objects manually. 

Note, however, that only one version can be activated for a single price list object. In case a newer version for your price list is activated, your previous version is assigned to the *Expired* state. Your version object can also be assigned to this status in case its corresponding price list is terminated.  

## Additional Information
Please refer to the [Pricing module documentation](https://connect.cloudblue.com/community/modules/pricing/) for more information  price list versions.
