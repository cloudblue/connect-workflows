# Inquiring Status
## Description
In case parameter value should be specified by tiers or provided parameter data in a tier request is not valid, the system can assign the *Inquiring* status to this request. Therefore, the Connect platform sends a form to specified tier contacts. Once this form is successfully filled out, the platform applies provided data and transfers the request to the *Pending* state.

Note that it is also possible to reject inquiring request and transfer them to the *Failed* state. In addition, the system enables to manually set tier requests to the *Pending* state.

## Prerequisites
An *Ordering* phase tier parameter is required to generate a request in this state. Alternatively, Vendors can mark provided parameter data as *invalid* and transfer their request to the *Inquiring* state.

Tier requests can also be assigned to this state from the following statuses:

* [Draft](s-a-draft.html)
* [Tiers Setup](s-c-tiers-setup.html)
## Transferable statuses
Once all required parameter data is submitted to tier requests, the system assigns such requests to the [Pending](s-b-pending.html) status. Otherwise, a tier request is rejected and assigned to the [Failed](s-f-failed.html) status.
## Associated transitions
* [New Inquiring Request](t-9-new-inquiring.html)
* [Inquiring Data](t-5-pend-inquiring.html)
* [Parameter Value Assignment](t-6-inq-pending.html) 
* [Tier Setup to Inquiring Transition](t-7-tier-inquiring.html) 
* [Draft to Inquiring Transition](t-11-draft-inquiring.html) 
* [Inquiring Request Rejection](t-13-inq-failed.html)