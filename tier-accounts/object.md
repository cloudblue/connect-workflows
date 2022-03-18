# Tier Accounts
## Description
Tier accounts represent objects that store customer or reseller account attributes. Creating tier accounts is required to specify customer and reseller information for subscriptions that are generated on the CloudBlue Connect platform. Additionally, note that that tier accounts are used to indicate the *current* state of reseller and customer data. Creating customer or reseller accounts is available for every type of account on the Connect platform.
Once a new tier account object is generated, the system assigns the *Active* status to this object. Therefore, the system allows utilizing customer and reseller data to generate subscriptions, create fulfillment request, and more. Note that Connect also enables to change customer or reseller data. Tier account object, however, remain in *Active* state. 
In case your tier accounts are removed, the system transfers such objects to the *Decommissioned* state. Therefore, such objects cannot be used to generate subscriptions or fulfillment request.

## Additional Information
Please refer to the [Customers Management Module](https://connect.cloudblue.com/community/modules/customers/) documentation from the Connect Community page for more details.
