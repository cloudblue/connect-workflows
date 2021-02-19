# Pending Request Status
## Description
The pending fulfillment request status represents a transient state assigned to a request when product fulfillment is pending. Vendors can approve or reject pending request. Furthermore, Vendors or the system can ask customer to fill out specified product parameters within this state. In case tiers setup is required, the system will transfer this request to the corresponding state.
## Subscription status
Pending fulfillment requests are interconnected with the following Subscription status:
**Processing**
## Prerequisites
A listed product and active distribution contract are required to create a pending fulfillment request. Fulfillment requests can also get the *pending* status from the following states:

* [Draft](s-a-draft.html)
* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
## Transferable statuses
In case any parameter data is required, a pending request can be switched to the [Inquiring](s-d-inquiring.html)) state.
If tier configuration is required, a request can get the [Tiers Setup](s-c-tiers-setup.html) status.
In case of on an error, a Vendor can reject a fulfillment request and assign the [Failed](s-f-failed.html) status to this request.
Once a Vendor appoves a fulfillment request, this request transfers to the [Approved](s-e-approved.html) state.
## Associated midway states
* [Pending Request Creation](t-1-new-pending.html)
* [Draft to Pending Convertion](t-3-draft-pending.html)
* [Pending to Tiers Setup Convertion](t-5-pending-tiers-setup.html)
* [Completed Tiers Configuration](t7-tiers-setup-pending.html)
* [System Parameters Inquiry](t8-pending-inquiring.html)
* [Vendor Parameters Inquiry](t9-pending-inquiring.html)
* [Inquiring Data Provision](t10-inquiring-pending.html)
* [Pending Request Approval](t11-pending-approved.html)
* [Pending Request Rejection](t-12-pending-failed)