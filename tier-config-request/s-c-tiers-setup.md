# Tiers Setup Status
## Description
The system displays the *Tier Setup* status for a Tier 1-level request in case its interconnected Tier 2-level request is created and not processed by Vendors. Thus, Vendors are required to locate and approve T2-level request first. Once this request is successfully approved, the system transfers the T1-level request from Tier Setup to the *Pending* state. Alternatively, in case the parameter value is inquired, the system transfers T1-level request to the *Inquiring* state.
## Prerequisites
A generated T2-level request is required to assign the status to a new tier request. Tier requests can also be assigned to this state from the [Draft](draft.html) status.
## Transferable statuses
Once the T2-level request is approved, T1-level request is assigned to one of the [Pending](s-b-pending.html) status statuses. However, in case the parameter value should be specified first, the request is assigned to the [Inquiring](s-d-inquiring.html) state.
In case a tiers request is rejected, this request is assigned to the [Failed](s-f-failed.html) status.
## Associated transitions
* [Tier Setup to Inquiring Transition](t-7-tier-inquiring.html) 
* [Completing Tier Setup](t-8-tier-pending.html)
* [New Tier Setup Request](t-10-new-tiers.html)
* [Draft to Tier Setup Transition](t-12-draft-tiers.html)
* [Tier Setup Request Rejection](t-16-tier-failed.html)
