# Processing Status 
## Description
This status indicates that a pending fulfillment request is created and Vendors are processing created subscription. 
Once Vendors approve the fulfillment request, the system activates this subscription and assigns corresponding status to it. In case Vendors reject the fulfillment request, the system assigns the *Terminated* status to the subscription. If Vendors transfer this fulfillment request to the *Inquiring* or *Tier Setup* state, this subscription remains in the *Processing* state. 
Furthermore, it is possible to create a draft subscription and transfer it to the *Processing* state in case the corresponding capability is enabled. 

## Fulfillment Requests
The processing subscriptions are interconnected with fulfillment requests in the following states:

* **Inquiring**
* **Tier Setup**
* **Pending**

## Prerequisites 
A listed product and an active distribution contract are required to create a pending request and a processing subscription.
## Transferable statuses
In case a fulfillment request is approved, the system assigns the [Active](s-b-active.html) status to a processing subscription.
If a fulfillment request is rejected, the system assigns the [Terminated](s-d-teminated.html) status.
## Associated transitions
* [Subscription Creation](t-1-new-subscription.html)
* [Subscription Approval](t-2-pro-active.html)
* [Subscription Rejection](t-3-pro-terminated.html)
* [Draft to Processing Convertion](t-12-draft-processing.html)