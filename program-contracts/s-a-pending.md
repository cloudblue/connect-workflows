# Pending Status 
## Description
Once a Distributor creates a new program contract, the system assigns the *Pending* status to it. This program contract remains in this state until it is signed and activated by a Vendor.
When a Vendor activates a pending program contract, the system transfers this contract to the *Active* state.
However, Vendors can also reject a pending program contract. Thus, the system transfers this contract to the *Rejected* state.
## Prerequisites
A program agreement is required to create a new program contract with the [Pending](s-a-pending.html) status.
## Transferable statuses
In case a Vendor signed program a contract, the system transfers it to the [Active](s-b-active.html) state.
If a Vendor rejected a contract, the system assigns the [Rejected](s-c-rejected.html) status to this contract.
## Associated transitions
* [Contract Creation](t-1-new-pending.html)
* [Contract Activation](t-2-pend-active.html)
* [Contract Rejection](t-3-pend-rejected.html)
* [Contract Removal](t-4-pend-deleted.html)
