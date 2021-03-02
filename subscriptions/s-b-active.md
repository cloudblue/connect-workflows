# Active Status
## Description
This subscription status indicates that a Vendor successfully approved a fulfillment request. Therefore, a Vendor provides required data (like product activation keys or URLs) to a consumer and the system assigns the *Active* status to the subscription.
An active subscription can be cancelled; thus, the system assigns the *Terminating* status to this subscription.
Once a subscription is activated, consumers might also create a change request to adjust items or item quantity.  
Furthermore, an active subscription can be suspended in case a corresponding capability is enabled.
## Fulfillment Requests
Active subscriptions are interconnected with fulfillment requests in the following state:
* **Approved**
In case a cancel fulfillment request receives the **Failed** status, an interconnected subscription remains in the *Active* state.
## Prerequisites
A subscription with the [Processing](s-a-processing.html) status and an approved fulfillment request.
## Transferable statuses
In case a cancel request is created, the active subscription is transferred to the [Terminating](s-c-terminating.html) state.
It is also possible to transfer active subscriptions to the [Suspended](s-e-suspended.html) state in case **Administrative Hold** capability is enabled.
## Associated transitions
* [Change Request Creation](t-6-change-request.html)
* [Change Request Approval](t-7-change-approval.html)
* [Subscription Suspension](t-8-suspend.html)
* [Subscription Resumption](t-9-resume.html)
* [Subscription Cancellation](t-4-active-terminating.html)