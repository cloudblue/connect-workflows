# Draft Request Status
## Description
The system assigns the *Draft* state to a new fulfillment request in case the dynamic validation capability is enabled. Therefore, the Connect platform enables its users to implement the real-time validation of tier configuration requests. Once a tier request is successfully validated, the system can transfer this request to the *Pending* status. Otherwise, this draft request is deleted.
## Prerequisites
The enabled **Dynamic Validation of Draft Request** product capability is required.
## Transferable statuses
The draft request can be transferred to one of the following statuses:

* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
* [Pending](s-b-pending.html)
## Associated transitions
* [New draft creation](t-2-new-draft.html)
* [Draft to Pending Request Convertion](t-3-draft-pending.html)
* [Draft Request Removal](t-4-draft-deleted.html)
