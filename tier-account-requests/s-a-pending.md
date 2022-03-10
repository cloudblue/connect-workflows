# Pending Status 
## Description
This status indicates that a new request to change or update tier account data is created. This state also indicates that the **Tier Accounts Sync** capability is switched on. Therefore, this tier account request remains in this state until it is accepted or ignored by Vendors.
## Prerequisites
* The enabled **Tier Accounts Sync** capability.
* Edited tier account data.

## Transferable statuses
Once a Vendor accepts a tier account request, the system transfers it to the [Accepted](s-c-accepted.html) state.
In case a Vendor ignores a request, the system assigns the [Ignored](s-d-ignored.html) status to this contract.
## Associated transitions
* [Pending Request Creation](t-1-new-pending.html)
* [Request Acceptance](t-3-pen-accepted.html)
* [Request Ignore](t-4-pen-ignored.html)
