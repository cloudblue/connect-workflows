# Failed Request Status 
## Description
he Failed fulfillment request status is displayed in case a generated fulfillment request is rejected by Vendors. This request state can also indicate that your Tier Configuration Request is failed or rejected. Therefore, the system will terminate any orders and will not perform operations that are specified in this request. Namely, in case a purchase request is rejected, the system terminates the subscription. Additionally, if a change request is cancelled, the system will not perform required subscription changes. 
Note that no further actions with failed requests are required. Note that the Connect platform can be used for further inspections and communication between partners regarding failed or rejected requests.
## Prerequisites
A fulfillment request can be transferred to the **Failed** state in case this request is assigned to one of the following statuses: 

* [Pending](s-b-pending.html)
* [Tiers Setup](s-c-tiers-setup.html)

## Associated transitions
* [Tier Configuration Failure](t-6-tiers-setup-failed.html)
* [Pending Request Rejection](t-12-pending-failed.html)
