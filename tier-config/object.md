# Tier Configuration
## Description
Tier Configuration (Tier Config) instances are used to assign configuration parameters to certain reseller accounts within the Distributor’s tiers hierarchy. These instances help partners manage and consolidate reseller information on the CloudBlue Connect platform. The system generates a tier configuration object and its associated tier request in case a specified product includes any **Tier Scope** parameter and a fulfillment request with this product is created.
Once a new tier config instance is created, the system assigns the *Processing* state to this tier config. Thereafter, Vendors are required to process a generated tier request and consequently transfer this tier config instance to the *Active* state.
Note that the Connect platform also allows implementing dynamic validation of draft tier request in case the corresponding product capability is enabled. Therefore, the system transfers new tier config instances to the *Draft* state. If draft configs are successfully validated, the system assigns the *Processing* status to them. Otherwise, draft configs are removed.
## Available Statuses
The list below displays available tier config statuses on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:

* A. [Draft](s-a-draft.html)
* B. [Processing](s-b-processing.html)
* C. [Active](s-c-active.html)
## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [New Processing Config](t-1-new-processing.html)
2. [Draft Config Creation](t-2-new-draft.html)
3. [Draft Config Validation](t-3-draft-processing.html)
4. [Draft Config Removal](t-4-draft-deleted.html)
5. [Config Activation](t-5-pro-active.html)
6. [Config Update](t-6-act-processing.html)


## Learn more
Refer to the [Connect community page](https://staging.connect.cloudblue.com/community/modules/tier-config/) for more information.
