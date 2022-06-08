# Verifying Status
## Description
Once your domain is added to the Connect platform, the system creates a new domain object and assigns it to the *Verifying* state. This status, as the name suggests, indicates that the system tries to verify your domain.

The verifying status is also assigned to your domain object in case reverification is required. This operation can be useful if the system returned an error.

When the system successfully verifies your domain, the domain object is assigned to the corresponding state. Otherwise, the system assigns your object to the *Verification Failed* or the *Verification Rejected* state depending on the occurred error.   
## Prerequisites
Your added domain on the CloudBlue Connect platform.
The system also allows reverifying domains and transfer such objects to the *Verifying* state again if necessary.

## Transferable statuses
Once your domain is verified successfully, the system assigns the domain object to the [Verified](s-b-verified.html) state.  
If the system cannot find required DNS record, your domain object is assigned to the [Verification Failed](s-d-failed.html) status.  
In case your specified domain name fails to asnwer the system's query, your domain object is assigned to
the [Verification Rejected](s-c-rejected.html) state.  
Note that verifying domain objects can be removed if necessary.
## Associated transitions
* [Domain Addition](t-1-new-pending.html)
* [Domain Verification](t-2-pend-inquiring.html)
* [Verified Domain Reverification](t-3-inq-pending.html)
* [Verification Rejection](t-4-pend-resolved.html)
* [Rejected Domain Reverification](t-5-res-pending.html)
* [Verification Failure](t-6-res-pending.html)
* [Domain Reverification](t-7-res-pending.html)
* [Domain Removal](t-8-res-pending.html)
