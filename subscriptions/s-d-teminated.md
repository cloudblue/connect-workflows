# Terminated Status 
## Description
The *Terminated* subscription status is displayed in case a Vendor rejects a fulfillment request. Therefore, this request is failed and an associated subscription is terminated.
Terminated subscription status can also indicate that a Vendor approved a cancel request. Buyers create such requests in case they want to cancel their subscription. Furthermore, cancel requests could be created from the Distributor or Vendor portals.
Note that the *Terminated* status represents a terminal state. No further actions with this subscriptions are required or available. 
## Fulfillment Requests
Terminated subscriptions are interconnected with fulfillment request in the following state:
**Failed**
In case a cancel request receives the **Active** status, an interconnected subscription is assigned to the *Terminated* state.
## Prerequisites
A subscription can be transferred to the *Terminated* state in case Vendors rejected a fulfillment request and this subscription is assigned to the [Processing](s-a-processing.html) state.
Furthermore, Vendors can approve a cancel request and transfer [Terminating](s-c-terminating.html) subscriptions to the *Terminated* state. 
## Associated transitions
* [Subscription Rejection](t-3-pro-terminated.html)
* [Cancellation Approval](t-5-terminating-terminated.html)
