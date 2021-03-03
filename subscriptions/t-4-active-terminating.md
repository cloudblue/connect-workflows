# Subscription Cancellation
## Description
This transition indicates that a request to cancel an active subscription was created. Thus, the system assigns the *Terminating* state to this subscription. Thereafter, Vendors can approve this cancel request and assign the *Terminated* status to the terminating subscription. Alternatively, Vendors can reject the request and return the subscription to the *Active* state.
## Prerequisites
A subscription with the [Active](s-b-active.html) status and a request to cancel a subscription.
## Operation results
A subscription with the [Terminating](s-c-terminating.html) status.