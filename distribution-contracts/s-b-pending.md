# Pending Status 
## Description
This status indicates that the system sucessfully processed the enrolling operation initiated by a Vendor. When the system assigns the *Pending* state to a distribution contract, Distributors can approve or reject this contract. Thereafter, the system transfers activated or rejected contracts to the corresponding states.
Note that Distributors can also ask Vendors to complete a custom form once again by clicking the **Refine Data** button. Thus, Vendors should complete this custom form and enroll their contract once again.
## Prerequisites
A distribution contract with the [Enrolling](s-a-enrolled.html) status.
## Transferable statuses
Once a Distributor approves a distribution contract, the system transfers it to the [Active](s-c-active.html) state.

If a Distributor rejects a distribution contract, the system assigns the [Rejected](s-d-rejected.html) status to this contract.

In case a Distributor clicks **Refine Data** from a pending distribution contract, the system transfers it back to the [Enrolling](s-a-enrolled.html) state.
## Associated transitions
* [Enrolling to Pending Contract Conversion](t-2-enr-pending.html)
* [Contract Activation](t-3-pen-active.html)
* [Contract Rejection](t-4-pen-rejected.html)
* [Data Refinement](t-6-pen-enrolling.html)
