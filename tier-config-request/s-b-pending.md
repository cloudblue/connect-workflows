# Pending Status
## Description
Once the system assigns the *Pending* status to tier requests, Vendors are required to process these pending requests. Depending on the Vendors actions, the system transfers these requests to the *Approved* state or the *Failed* state. Note that the system assigns the *Pending* status to a new draft request in case it is successfully validated by Distributors. Furthermore, note that Vendors can also inquire parameter data and consequently transfer a pending request to the *Inquiring* state.

## Prerequisites
A tier request is generated in case a **Tier scope product parameter** is presented and a *fulfillment request* is created. Tier requests can also be assigned to the *pending* status from the following states:

* [Draft](s-a-draft.html)
* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
## Transferable statuses
In case any parameter data is required, a pending request can be switched to the [Inquiring](s-d-inquiring.html)) state.
In case of on an error, the system asllows rejecting a pending request and assign it to the [Failed](s-f-failed.html) status.
Once a Vendor appoves a tier request, this request transfers to the [Approved](s-e-approved.html) state.
## Associated transitions
* [Pending Request Creation](t-2-new-pending.html)
* [Draft Validation](t-4-draft-pending.html)
* [Inquiring Data](t-5-pend-inquiring.html)
* [Parameter Value Assignment](t-6-inq-pending.html) 
* [Completing Tier Setup](t-8-tier-pending.html)
* [Request Approval](t-14-pend-approved.html)
* [Pending Request Rejection](t-15-pend-failed.html)
* 
