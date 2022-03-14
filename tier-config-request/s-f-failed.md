# Failed Status 
## Description
In case Vendors or Distributors reject a tier configuration request, the system assigns the *Failed* status to this request. Therefore, its interconnected fulfillment request will be also assigned to the *Failed* status. Provided changes within a failed *update* tier request will also not be implemented. Note that this status represents a terminal state, meaning no actions with failed requests are available or required.
## Prerequisites
A tier request can be transferred to the **Failed** state in case this request is assigned to one of the following statuses: 

* [Pending](s-b-pending.html)
* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.hmtl)
## Associated transitions
* [Tier Setup Request Rejection](t-16-tier-failed.html) 
* [Pending Request Rejection](t-12-pending-failed)
* [Inquiring Request Rejection](t-13-inq-failed.html)
