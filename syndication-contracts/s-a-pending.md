# Pending Status 
## Description
Once Resellers enroll a new syndication contract, the system assigns the *Pending* status to this contract. It remains in this state until it is signed and activated by the corresponding syndication Distributor.
In case this Distributor activates a pending syndication contract, the system transfers this contract to the *Active* state.
However, the Distributor can also reject a pending contract. Therefore, the system transfers this contract to the *Rejected* state.
## Prerequisites
A syndication agreement is required to create a new contract with the [Pending](s-a-pending.html) status.
## Transferable statuses
In case Resellers sign a contract, the system transfers it to the [Active](s-b-active.html) state.
If Reseller reject a contract, the system assigns the [Rejected](s-c-rejected.html) status to this contract.
## Associated transitions
* [Contract Creation](t-1-new-pending.html)
* [Contract Activation](t-2-pend-active.html)
* [Contract Rejection](t-3-pend-rejected.html)
