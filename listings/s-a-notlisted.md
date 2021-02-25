# Not Listed Status 
## Description
The **Not Listed** state indicates that a specified listing is not activated. 
Once a Vendor creates a listing request and it is not completed by Distributors, this listing provides the **Not Listed** status. In case Distributors deploy a product and mark this listing request as *Completed*, the system assigns the **Listed** status to the listing. Otherwise, Distributors reject the request and the listing will remain in the **Not Listed** state. 
Furthermore, Vendors can create a request to terminate activated listing. Therafter, Distributors can complete this request and transfer this listing to the **Not Listed** state. 
## Listing Requests
Listings in this state are interconnected with one of the following Listing Request statuses:

* **Reviewing**
* **Deploying**
* **Cancelled**
## Prerequisites 
A submitted listing request is required for Connect to create a new listing with this status.
## Transferable statuses
Once Distributors deploy a specified product and mark a provided listing request as *Completed*, the listing assigns to the [Listed](s-b-listed.html) status. 
## Associated transitions
* [Listing Creation](t-1-new-notlisted.html)
* [Listing Approval](t-2-notlisted-listed.html)
* [Listing Rejection](t-3-notlisted.html)
* [Termination Apporoval](t-5-listing-termination.html)