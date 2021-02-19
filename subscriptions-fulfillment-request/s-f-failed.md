# Failed Request Status 
## Description
The failed fulfillment request status is displayed in case a fulfillment request created by a buyer was rejected by a Vendor. Furthermore, this status is displayed in case the tiers configuration is failed. Note that the failed request status is a teminal state, meaning **failed fulfillment requests could not be restored**. Therefore, it is recommended to reject such requests only in case of an unrecoverable error.
## Subscription status
Failed subscription requests are interconnected with the following Subscription status:
**Terminated**
## Prerequisites
A fulfillment request can be transferred to the **Failed** state in case this request is assigned to one of the following statuses: 

* [Pending](s-b-pending.html)
* [Tiers Setup](s-c-tiers-setup.html)
## Associated midway states
* [Tier Configuration Failure](t-6-tiers-setup-failed)
* [Pending Request Rejection](t-12-pending-failed)