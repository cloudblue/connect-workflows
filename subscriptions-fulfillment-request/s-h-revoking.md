# Revoking Request Status 
## Description
In case Distributors or Resellers revoke a scheduled fulfillment request, the system assigns the Revoking status to this request. Thus, the delayed request activation procedure will be canceled. This allows Vendors to clean up resources that are required for subscription activation. Note that if the system assigns the Revoking status to your request, it cannot be assigned back to the Scheduled or Pending state. 
Furthermore, Vendors are required to confirm their request revocation. Once your request revocation is confirmed, the system automatically assigns the *Revoked* status to your revoking request.
## Prerequisites
A fulfillment request that is assigned to the [Scheduled](s-g-scheduled.html) status.
## Transferable statuses
In case Vendors confirm their request revocation, the system transfers this request to the [Revoked](s-i-revoked.html) state.
## Associated transitions
* [Request Revocation](t-15-scheduled-revoking.html)
* [Revocation Confirmation](t-16-revoked-revoked.html)
