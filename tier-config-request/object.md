# Tier Configuration Requests
## Description
Tier Configuration Requests (Tier Requests) represent instances on the CloudBlue Connect platform that allow Partners to consolidate *setup* or *update* operations for **Tier Configurations**. 
The system generates a tier configuration instance and a tier request in case a **Tier scope product parameter** is presented and a *fulfillment request* is created. Therefore, the system can generate *setup requests* in case a new tier configuration is created and *update requests* in case provided tier configuration should be updated.
The system assigns the *Pending* status to new tier requests. Vendors can approve or reject requests and transfer tier requests to corresponding states. In case a tier request validation capability is enabled, the system assigns new request to the Draft state. Note that in case parameter value should be specified, such tier requests are assigned to the *Inquiring* state.
Furthermore, note that the system can generate T1-level and T2-level requests and corresponding tier configurations depending on specified product parameters. In case your product includes both Tier 1 and Tier 2 parameters, the system transfers Tier 1-level request to the *Tier Setup* state.

## Tier request statuses
The list below displays available statuses for tier configuration requests on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:

* A. [Draft](s-a-draft.html)
* B. [Pending](s-b-pending.html)
* C. [Tiers Setup](s-c-tiers-setup.html)
* D. [Inquiring](s-d-inquiring.html)
* E. [Approved](s-e-approved.html)
* F. [Failed](s-f-failed.html)
## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [New Draft Creation](t-1-new-draft.html)
2. [Pending Request Creation](t-2-new-pending.html)
3. [Draft Removal](t-3-draft-deleted.html)
4. [Draft Validation](t-4-draft-pending.html)
5. [Inquiring Data](t-5-pend-inquiring.html)
6. [Parameter Value Assignment](t-6-inq-pending.html) 
7. [Tier Setup to Inquiring Transition](t-7-tier-inquiring.html) 
8. [Completing Tier Setup](t-8-tier-pending.html)
9. [New Inquiring Request](t-9-new-inquiring.html)
10. [New Tier Setup Request](t-10-new-tiers.html)
11. [Draft to Inquiring Transition](t-11-draft-inquiring.html) 
12. [Draft to Tier Setup Transition](t-12-draft-tiers.html)
13. [Inquiring Request Rejection](t-13-inq-failed.html)
14. [Tier Request Approval](t-14-pend-approved.html)
15. [Pending Request Rejection](t-15-pend-failed.html) 
16. [Tier Setup Request Rejection](t-16-tier-failed.html) 
## Learn more
Refer to the [Connect community page](https://connect.cloudblue.com/community//tier-config/) for more information.
