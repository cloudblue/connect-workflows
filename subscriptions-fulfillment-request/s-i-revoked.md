# Revoked Request Status 
## Description
The Revoked status indicates that Vendors confirmed the revocation of their fulfillment request. This status also indicates that Vendors successfully cleaned up all resources that could have been prepared for subscription processing.
Note that the Revoked request status represents a terminal state. Namely, revoked fulfillment requests cannot be restored back to the Scheduled or Pending state. In addition, no further actions with revoked requests are required or available.
## Prerequisites
A fulfillment request that is assigned to the [Revoking](s-h-revoking.html) status.
## Associated transition
* [Revocation Confirmation](t-16-revoked-revoked.html)
