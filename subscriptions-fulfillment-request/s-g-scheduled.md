# Scheduled Request Status 
## Description
The Connect platform enables Vendors to schedule time and date for their request processing. Namely, the Scheduled status is used to explicitly define a waiting period before processing fulfillment requests. Therefore, it allows businesses that collaborate on Connect to synchronize their workflows and avoid undesirable situations in which a subscription can be cancelled while Vendors could have made all required preparations. 
The system allows Distributors or Resellers to revoke scheduled requests and cancel delayed request activation. Therefore, the system assigns the *Revoking* status to such requests. Otherwise, scheduled requests can be assigned back to the Pending state.
## Prerequisites
A fulfillment request that is assigned to the [Pending](s-b-pending.html) status.
## Transferable statuses
In case Distributors or Resellers revoke a scheduled request, the system automatically transfers it to the [Revoking](s-h-revoking.html) status.
Otherwise, scheduled requests can be transferred back to the [Pending](s-b-pending.html) status.
## Associated transitions
* [Schedule Delayed Activation](t-13-pending-scheduled.html)
* [Scheduled to Pending Convertion](t-14-scheduled-pending.html)
* [Request Revocation](t-15-scheduled-revoking.html)
