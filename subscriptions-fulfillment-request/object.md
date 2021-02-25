# Subscriptions / Fulfillment Requests
## Description
Fulfillment requests (or Subscription requests) represent product orders that are originated from Provider’s commerce systemd and sent to Vendors. To process fulfillment requests, Vendors require information not only relative to their product, but also about the customer, supply chain, marketplaces, etc. Therefore, the Connect platform stores and provides all required data to process fullfillment requests.
Fulfillment requests are interconnected with Subscriptions, and these requests are stored within the Subscriptions module. Thus, for instance, a purchase request create a subscription, while a cancel request terminate it. However, **Fulfillment requests should not be confused with Subscriptions** as they represent different objects within the Connect platform.
## Fulfillment request statuses
The list below displays available statuses for fulfillment requests on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:
A. [Draft](s-a-draft.html)
B. [Pending](s-b-pending.html)
C. [Tiers Setup](s-c-tiers-setup.html)
D. [Inquiring](s-d-inquiring.html)
E. [Approved](s-e-approved.html)
F. [Failed](s-f-failed.html)
## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:
1. [Pending Request Creation](t-1-new-pending.html)
2. [Draft Request Creation](t-2-new-draft.html)
3. [Draft to Pending Convertion](t-3-draft-pending.html)
4. [Draft Request Removal](t-4-draft-deleted.html)
5. [Pending to Tiers Setup Convertion](t-5-pending-tiers-setup.html)
6. [Tier Configuration Failure](t-6-tiers-setup-failed.html)
7. [Completed Tiers Configuration](t7-tiers-setup-pending.html)
8. [System Parameters Inquiry](t8-pending-inquiring.html)
9. [Vendor Parameters Inquiry](t9-pending-inquiring.html)
10. [Inquiring Data Provision](t10-inquiring-pending.html)
11. [Pending Request Approval](t11-pending-approved.html)
12. [Pending Request Rejection](t-12-pending-failed.html)
## Learn more
Refer to the [Connect community page](https://connect.cloudblue.com/community/subscriptions) for more information.
