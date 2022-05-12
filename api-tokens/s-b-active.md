# Active Status
## Description
The *Active* status indicates that your API token can be used for subsequent operations. This status is automatically assigned to pending token objects by the system, once they are processed successfully. The system enables users to disable their active tokens. Users can also reactivate their inactive tokens if necessary.
## Prerequisites 
A new token with the [Pending](s-a-pending.html) status.
Operators can also reactivate their tokens in the [Inactive](s-c-inactive.html) state.
## Transferable statuses
In case your token object is disabled, it is transferred to the [Inactive](s-c-inactive.html) state.
If operators decide to delete their active token, this token is assigned to the [Deleted](s-d-deleted.html) state.
## Associated transitions
* [Token Activation](t-2-pen-active.html)
* [Token Deactivation](t-3-act-inactive.html)
* [Token Reactivation](t-4-in-active.html)
* [Token Removal](t-5-token-deleted.html)
