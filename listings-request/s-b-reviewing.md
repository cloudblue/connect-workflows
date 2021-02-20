# Reviewing Request Status
## Description
The reviewing listing request status indicates that Vendors sent their listing request to Distributors for a review. Thereafter, Distributors can approve this listing request and initiate the product deployment procedure. Otherwise, Distributors reject to proceed with this deployment and this listing request transfers to the *Cancelled* state.
## Listing status
Reviewing listing requests are interconnected with the following Listing status:
**Not Listed**
## Prerequisites
A submitted listing requests from the [Draft](draft.html) state.
## Transferable statuses
Once a Distributor initiate the product deployment operation, a reviewing listing request is assigned to the [Deploying](deploying.html) status.
Otherwise, this listing request and transfer it to the [Cancelled](cancelled.html) state.
## Associated midway states
* [Draft to Reviewing Request Convertion](t-3-draft-reviewing.html)
* [Reviewing Request Approval](t-4-reviewing-deploying.html)
* [Reviewing Request Rejection](t-7-reviewing-cancelled)