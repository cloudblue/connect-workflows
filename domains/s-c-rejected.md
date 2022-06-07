# Verification Rejected Status
## Description
This status is assigned to your domain object in case the domain verification is rejected due to the *SERVFAIL* error. Specifically, this error implies that your added domain failed to answer the query of the CloudBlue Connect platform.

In case of this error, please make sure that your specified domain name is correct and try to reverify your added domain. 
## Prerequisites
A domain object with the [Verifying](s-a-verifying.html) status.
## Transferable statuses
In case your domain should be reverified, the system transfers the domain object back to the [Verifying](s-a-verifying.html) state.
Domain objects in this status can also be deleted if it is necessary.
## Associated transitions
* [Verification Rejection](t-4-pend-resolved.html)
* [Rejected Domain Reverification](t-5-res-pending.html)
* [Domain Removal](t-8-res-pending.html)
