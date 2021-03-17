# Draft Status 
## Description
This status indicates that a Vendor created a product instance on the Connect platform. Furthermore, this status indicates that a Vendor specifies product data and configures a product, but this product does not have a version yet. 
Once all required product information is specified and the Product Definition is complete, Vendor creates a version for this product. Therefore, the Connect platform assigns this draft product with the *Published* state.
Otherwise, a Vendor deletes a draft; thus, all provided product information and configuration is removed. 
## Prerequisites 
An active distribution contract is required to create a new draft product.
## Transferable statuses
In case a Vendor assigns a version to a product with this status, the system transfers this product to the [Published](s-b-listed.html) state.
## Associated transitions
* [Draft Creation](t-1-new-draft.html)
* [Product Version Assignment](t-2-draft-pub.html)
* [Draft Removal](t-3-draft-del.html)
