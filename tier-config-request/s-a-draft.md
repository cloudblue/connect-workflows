# Draft Status
## Description
The system assigns the *Draft* state to a new tier request in case the dynamic validation capability is enabled. Therefore, the Connect platform enables users to implement the real-time validation of tier configuration requests. Once a tier request is successfully validated, the system can transfer this request to the *Pending*, *Inquiring*, or *Tier Setup* status. Otherwise, this draft request is deleted.
## Prerequisites
This status is assigned to new tier requests in case the **Dynamic Validation – Tier Config Request – Draft** product capability is enabled.
## Transferable statuses
Draft requests can be deleted or transferred to one of the following statuses:

* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
* [Pending](s-b-pending.html)
## Associated transitions
* [New Draft Creation](t-1-new-draft.html)
* [Pending Request Creation](t-2-new-pending.html)
* [Draft Removal](t-3-draft-deleted.html)
* [Draft Validation](t-4-draft-pending.html)
* [Draft to Inquiring Transition](t-11-draft-inquiring.html) 
* [Draft to Tier Setup Transition](t-12-draft-tiers.html)