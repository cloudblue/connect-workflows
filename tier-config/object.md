# Tier Configuration
## Description
Tier Configuration (Tier Config) instances are used to assign configuration parameters to certain reseller accounts within the Distributor’s tiers hierarchy. These instances help partners manage and consolidate reseller information on the CloudBlue Connect platform. The system generates a tier configuration object and its associated tier request in case a specified product includes any **Tier Scope** parameter and a fulfillment request with this product is created.
Once a new tier config instance is created, the system assigns the *Processing* state to this tier config. Thereafter, Vendors are required to process a generated tier request and consequently transfer this tier config instance to the *Active* state.
Note that the Connect platform also allows implementing dynamic validation of draft tier request in case the corresponding product capability is enabled. Therefore, the system transfers new tier config instances to the *Draft* state. If draft configs are successfully validated, the system assigns the *Processing* status to them. Otherwise, draft configs are removed.

## Additional Information
Please refer to the [Tier Config Management module](https://connect.cloudblue.com/community/modules/tier-config/) documentation for more information.
