# Verification Failed Status
## Description
The *Verification Failed* status indicates that the system cannot verify your added domain. In this case, please make sure that your provided DNS records are specified correctly. 

Furthermore, note that DNS changes can take a while to be applied. It is recommended to wait a few hours, reopen your domain and try to verify it again. 

In case the system still fails the verification operation, please try adding a different DNS TXT record.
## Prerequisites
A domain object with the [Verifying](s-a-verifying.html) status.
## Associated transitions
* [Verification Failure](t-6-res-pending.html)
* [Domain Reverification](t-7-res-pending.html)
* [Domain Removal](t-8-res-pending.html)
