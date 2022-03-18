# Listing Requests
## Overview
A *listing request* object represents a formal request to list a product on a specified marketplace. Listing requests contain product specifications, associated price lists, and included product offers. 
The system allows Vendors to generate listing requests of the following types: *create* (requests to list a new product), *update* (requests to update listing data), or delete (requests to delist a product from the marketplace). Consequently, all listing requests should be processed by Distributors/ Resellers.

Once a new listing request object is generated, the system assigns the *Draft* status to this object. Once Vendors submit their request to Distributor or Reseller systems, the request object is automatically assigned to the *Reviewing* state. Distributors or Resellers can start processing the request and transfer it to the *Deploying* state. In case the request processing is successful, Distributors/Resellers assign the *Completed* status to this request. Alternatively, Distributors/Resellers can reject request in case of an error and transfer it to the *Cancelled* state.

## Additional Information
Please refer to the [Listings Management Module](https://connect.cloudblue.com/community/modules/listings/) documentation for more information.
