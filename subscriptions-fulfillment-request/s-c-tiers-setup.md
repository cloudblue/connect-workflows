# Tiers Setup Request Status
## Description
In case reseller or customer account configuration is required, the system transfers corresponding fulfillment requests to the Tier Setup state. The system also generates a Tier Configuration object and its Tier Request that should be also processed and consolidated via the corresponding module on the Connect platform. 

Once a tier request is successfully approved and tier configuration is activated, the system transfers your fulfillment request to the Pending state and sends **Tier Configuration Approved Template** to your customers or resellers. Refer to the [Tier Configuration documentation](https://connect.cloudblue.com/community/modules/tier-config/) for more information. 
## Prerequisites
A listed product and active distribution contract are required to create a fulfillment request with *tiers setup* status. Fulfillment requests can also get this status from the [Draft](draft.html) state.

## Transferable statuses
Once the tiers configuration is successfully completed, your fulfillment request can be assigned to one of the following statuses:

* [Pending](s-b-pending.html)
* [Inquiring](s-d-inquiring.html)

In case the tiers configuration is failed, this request is assigned to the [Failed](s-f-failed.html) status.
## Associated transitions
* [Pending to Tiers Setup Convertion](t-5-pending-tiers-setup.html)
* [Tier Configuration Failure](t-6-tiers-setup-failed)
* [Completed Tiers Configuration](t-7-tiers-setup-pending.html)
