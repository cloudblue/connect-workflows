# Deploying Request Status
## Description
The Deploying listing request status is displayed in case a Distributor/ Resellers marked this listing request as Deploying. Therefore, Distributors or Resellers make all required preparations to deploy a product to their marketplace, update. Otherwise, Distributors/ Resellers reject the request, the system transfers the request object to the *Cancelled* state.
## Listing status
Deploying listing requests are interconnected with the following Listing status:
**Not Listed**
## Prerequisites
A listing requests in the [Reviewing](reviewing.html) state.
## Transferable statuses
Once a Distributor finishes the product deployment operation, a deploying listing request can be assigned to the [Completed](completed.html) status.
In case of an error, Distributor can also reject a listing request and assign the [Cancelled](cancelled.html) status to this request.
## Associated transitions
* [Reviewing Request Approval](t-4-reviewing-deploying.html)
* [Deployment Completion](t-5-deploying-completed.html)
* [Deployment Cancellation](t-6-deploying-cancelled.html)
