# Verified Status
## Description
The *Verified* status indicates that your domain is verified successfully. Therefore, the Single Sign-On functionality will be avaiable for your organization. 

Once your domain is verified successfully, it is highly recommended to systematically reverify your domain on Connect platform in order to prevent possible issues with your SSO authorization.

It is also important to note that one Connect account can also include several verified domains. In addition, multiple Connect accounts can also belong to the same verified domain.
## Prerequisites
A domain object with the [Verifying](s-a-verifying.html) status.
## Transferable statuses
In case your domain should be reverified, the system transfers the domain object back to the [Verifying](s-a-verifying.html) state.  
Verified domain objects can also be removed if necessary.
## Associated transitions
* [Domain Verification](t-2-pend-inquiring.html)
* [Verified Domain Reverification](t-3-inq-pending.html)
* [Domain Removal](t-8-res-pending.html)
