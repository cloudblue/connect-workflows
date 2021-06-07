# Tiers Setup Request Status
## Description
The *Tiers Setup* fulfillment request status indicates that this fulfillment request requires Vendors to process tier configuration first. Tier configuration requests can be successfully approved or failed. Therefore, depending on the following Vendor actions with this request, fulfillment request can be assigned to the *Pending* status or to the *Failed* status. Refer to the [Connect community page](https://connect.cloudblue.com/community/modules/tier-config/) to learn more about tier configuration. 
## Subscription status
Fulfillment requests with the *tiers setup* status are interconnected with the following Subscription status:
**Processing**
## Prerequisites
A listed product and active distribution contract are required to create a fulfillment request with *tiers setup* status. Fulfillment requests can also get this status from the [Draft](draft.html) state.
## Transferable statuses
Once the tier configuration request processing is completed, the fulfillment request is assigned to one of the following statuses:

* [Pending](s-b-pending.html)
* [Inquiring](s-d-inquiring.html)

In case the tiers configuration is failed, this request is assigned to the [Failed](s-f-failed.html) status.
## Associated transitions
* [Pending to Tiers Setup Convertion](t-5-pending-tiers-setup.html)
* [Tier Configuration Failure](t-6-tiers-setup-failed)
* [Completed Tiers Configuration](t7-tiers-setup-pending.html)
