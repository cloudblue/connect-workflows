# Tier Configuration Requests
## Description
Tier Configuration Requests (Tier Requests) represent instances on the CloudBlue Connect platform that allow Partners to consolidate *setup* or *update* operations for **Tier Configurations**. 
The system generates a tier configuration instance and a tier request in case a **Tier scope product parameter** is presented and a *fulfillment request* is created. Therefore, the system can generate *setup requests* in case a new tier configuration is created and *update requests* in case provided tier configuration should be updated.
The system assigns the *Pending* status to new tier requests. Vendors can approve or reject requests and transfer tier requests to corresponding states. In case a tier request validation capability is enabled, the system assigns new request to the Draft state. Note that in case parameter value should be specified, such tier requests are assigned to the *Inquiring* state.
Furthermore, note that the system can generate T1-level and T2-level requests and corresponding tier configurations depending on specified product parameters. In case your product includes both Tier 1 and Tier 2 parameters, the system transfers Tier 1-level request to the *Tier Setup* state.

## Additional Information
Please refer to the [Tier Config Management Module](https://connect.cloudblue.com/community//tier-config/) documentation for more information.
