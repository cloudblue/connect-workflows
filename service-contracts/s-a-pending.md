# Pending Status 
## Description
Once a Distributor creates a new service contract, the system assigns the *Pending* status to it. This service contract remains in this state until it is signed and activated by a Reseller.
When a Reseller activates a pending service contract, the system transfers this contract to the *Active* state.
However, Resellers can also reject a pending service contract. Thus, the system transfers this contract to the *Rejected* state.
## Prerequisites
A service agreement is required to create a new service contract with the [Pending](s-a-pending.html) status.
## Transferable statuses
In case a Reseller signed service a contract, the system transfers it to the [Active](s-b-active.html) state.
If a Reseller rejected a contract, the system assigns the [Rejected](s-c-rejected.html) status to this contract.
## Associated transitions
* [Contract Creation](t-1-new-pending.html)
* [Contract Activation](t-2-pend-active.html)
* [Contract Rejection](t-3-pend-rejected.html)
* [Contract Removal](t-4-pend-deleted.html)
