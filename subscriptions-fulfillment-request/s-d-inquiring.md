# Inquiring Request Status
## Description
The Inquiring request status in case product parameter specification is required. These parameters enable Vendors to meet specific product fulfillment requirements (e.g., specifying a phone number or email address). The parameters parameters can be inquired by the system or by Vendors. Thus, the system transfers a pending request to this state until the parameter data is submitted. Furthermore, the system also sends your specified Inquiring Template to your customers or resellers. 
Once all required parameter data is presented, the system transfers the request back to the *Pending* status. Therefore, Vendors will be able to process this fulfillment request.

## Prerequisites
A listed product and active distribution contract are required to create an inquiring fulfillment request. Fulfillment requests can also get the *Inquiring* status from the following states:

* [Draft](s-a-draft.html)
* [Tiers Setup](s-c-tiers-setup.html)

## Transferable statuses
In case all required parameter data is submitted, this fulfillment request is assigned to the [Pending](s-b-pending.html) status.
## Associated transitions
* [System Inquiry](t-8-pending-inquiring.html)
* [Vendor Inquiry](t-9-pending-inquiring.html)
* [Inquiring Data Provision](t-10-inquiring-pending.html)
