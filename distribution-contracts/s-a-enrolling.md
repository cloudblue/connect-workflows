# Enrolling Status 
## Description
This status indicates that a Vendor enrolled a distribution agreement and consequently enrolled a distribution contract. Thus, the CloudBlue Connect platform generates a distribution contract based on this enrolled distribution agreement and assigns the *Enrolling* status to the contract. Thereafter, the system transfers this contract to the *Pending* state.
In case Distributors attach **Custom Forms** to this distribution agreement, Vendors should specify required information to successfully enroll their distribution contract. 
Note that Distributors can also ask Vendors to complete the submitted form once again and transfer their distribution contract back to the *Enrolling* state.
## Prerequisites 
A distribution agreement that is created by Distributors and enrolled by Vendors.
## Transferable statuses
Once the distribution contract enrolling operation is processed, the system changes the contract status to [Pending](s-b-pending.html).
## Associated transitions
* [Contract Enrollment](t-1-new-enrolling.html)
* [Enrolling to Pending Conversion](t-2-enr-pending.html)
* [Data Refinement](t-6-pen-enrolling.html)
