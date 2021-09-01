# Active Status
## Description
Once a new customer or reseller account is created on the Connect platform, the system generates a new tier account object and assigns it to the *Active* state. Therefore, tier account objects in this state can be used to generate subscriptions, create or manage fulfillment request, and more. 
The system allows editing customer or reseller information that is provided in your tier account objects. In case such information is updated, your tier account object remains in the *Active* state.
In addition, note that tier account objects can be deleted by using provided graphical user interface or Connect API.  
## Prerequisites
A new created customer or reseller account.
## Transferable statuses
Once your active customer or reseller account is removed, the system assigns your tier account object to the [Decommissioned](s-b-decom.html) state.
## Associated transitions
* [Tier Account Creation](t-1-new-active.html)
* [Tier Account Removal](t-2-act-decom.html)
