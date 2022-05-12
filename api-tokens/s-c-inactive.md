# Inactive Status 
## Description
In case operators disable their token on the Connect platform, the system assigns the *Inactive* status to this token. This status indicates that your token cannot be used for integrations or any other operations with API. In case an inactive token is used for such operations, the system will return an error. Inactive tokens can be activated again or removed if necessary 
## Prerequisites
A token object with the [Active](s-b-active.html) status.
# Transferable statuses
In case your token object is enabled again, the system transfers it the [Active](s-b-active.html) state.
If operators decide to delete their inactive token, this token is assigned to the [Deleted](s-d-deleted.html) state.
## Associated transitions
* [Token Deactivation](t-3-act-inactive.html)
* [Token Reactivation](t-4-in-active.html)
* [Token Removal](t-5-token-deleted.html)
