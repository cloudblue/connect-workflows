# Reviewing Request Status
## Description
The Reviewing listing request status indicates that Vendors sent their listing request to Distributors for a review. Thereafter, Distributors can approve this listing request and consequently activate product listing, update listing information or delete listing. Otherwise, Distributors or Resellers can and this listing request transfers to the *Cancelled* state.
## Listing status
Reviewing listing requests are interconnected with the following Listing status:
**Not Listed**
## Prerequisites
A submitted listing requests from the [Draft](draft.html) state.
## Transferable statuses
Once a Distributor initiate the product deployment operation, a reviewing listing request is assigned to the [Deploying](deploying.html) status.
Otherwise, this listing request and transfer it to the [Cancelled](cancelled.html) state.
## Associated transitions
* [Draft to Reviewing Request Convertion](t-3-draft-reviewing.html)
* [Reviewing Request Approval](t-4-reviewing-deploying.html)
* [Reviewing Request Rejection](t-7-reviewing-cancelled)
