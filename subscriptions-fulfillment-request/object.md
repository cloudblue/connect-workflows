# Subscriptions / Fulfillment Requests
## Description
Fulfillment requests (or Subscription requests) represent product orders that are originated from Provider’s commerce systemd and sent to Vendors. To process fulfillment requests, Vendors require information not only relative to their product, but also about the customer, supply chain, marketplaces, etc. Therefore, the Connect platform stores and provides all required data to process fullfillment requests.
Fulfillment requests are interconnected with Subscriptions, and these requests are stored within the Subscriptions module. Thus, for instance, a purchase request create a subscription, while a cancel request terminate it. However, **Fulfillment requests should not be confused with Subscriptions** as they represent different objects within the Connect platform.
## Request statuses
The list below displays available statuses for fulfillment requests on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:
* [Draft](s-a-draft.html)
* [Pending](s-b-pending.html)
* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
* [Approved](s-e-approved.html)
* [Failed](s-f-failed.html)
## Midway states
Choose a midway state from the provided diagram or click on any of the following contextual links to access midway state information:
* [Pending Request Creation](t-1-new-pending.html)
* [Draft Request Creation](t-2-new-draft.html)
* [Draft to Pending Convertion](t-3-draft-pending.html)
* [Draft Request Removal][t-4-draft-deleted]
* [Pending to Tiers Setup Convertion](t-5-pending-tiers-setup.html)
* [Tier Configuration Failure](t-6-tiers-setup-failed)
* [Completed Tiers Configuration](t7-tiers-setup-pending.html)
* [System Parameters Inquiry](t8-pending-inquiring.html)
* [Vendor Parameters Inquiry](t9-pending-inquiring.html)
* [Inquiring Data Provision](t10-inquiring-pending.html)
* [Pending Request Approval](t11-pending-approved.html)
* [Pending Request Rejection](t-12-pending-failed)
## Learn more
Refer to the [Connect community page](https://connect.cloudblue.com/community/subscriptions) for more information.