# Pending Status
## Description
Once a new token is created, the system assigns the *Pending* status to this object. This status indicates that the system is processing your token object. Therefore, when the system successfully processes your token, it will be assigned to the following state.
## Prerequisites 
A new created token object ios required.
## Transferable statuses
Once the system processes the pending token object, it is assigned to the [Active](s-b-active.html) state.
In case operators decide to delete their pending token, this token is assigned to the [Deleted](s-d-deleted.html) state.
## Associated transitions
* [Token Creation](t-1-new-pending.html)
* [Token Activation](t-2-pen-active.html)
* [Token Removal](t-5-token-deleted.html)
