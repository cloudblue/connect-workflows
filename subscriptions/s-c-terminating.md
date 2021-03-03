# Terminating Status 
## Description
This subscription status is displayed in case a buyer created a request to cancel a subscription. These requests can be also emulated from Vendor or Distributor portals. 
Once Vendors approve this cancellation request, a terminating subscription is transferred to the *Terminated* state.
In case Vendors reject this request, the subscription returns to the *Active* state and the request gets the *Failed* status.
## Prerequisites
A subscription in the [Active](s-b-active.html) state and a cancel request.
## Transferable statuses
In case a cancel request is apporived, the system assigns the [Terminated](s-d-teminated.html) status to a terminating subscription. 
If this request is rejected, the system assigns the [Active](s-b-active.html).
## Associated transitions
* [Subscription Cancellation](t-4-active-terminating.html)
* [Cancellation Approval](t-5-terminating-terminated.html)
