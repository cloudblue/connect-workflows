# Suspended Status 
## Description
This subscription status is displayed in case a suspend request is created and approved. Thereafter, it is possible to create a resume request and reactivate suspended subscription by approving the resume request. Note that suspend and resume requests are available in case the **Administrative Hold** capability is enabled. Refer to the [Connect community portal](https://connect.cloudblue.com/community/modules/products/capabilities/) to learn more about capability attributes.
## Prerequisites
A subscription in the [Active](s-b-active.html) state.
## Transferable statuses
Once a resume request is created, a suspended subscription returns to the [Active](s-b-active.html) state.
## Associated transitions
* [Subscription Suspension](t-8-suspend.html)
* [Subscription Resumption](t-9-resume.html)