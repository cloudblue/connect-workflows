# Pending Status
## Description
Once a Connect user decides to report an issue or a request on the Connect platform, the system creates a new Helpdesk Case and automatically assigns the *Pending* status to this Case. 
When your Case is assigned to this state, the system allows inquiring necessary data from your Partners. Therefore, this Case will be assigned to the *Inquiring* state.
In addition, note that the system can also transfer an inquiring Case to the *Pending* state if all required information is presented. 
If your Case is successfully resolved, the system also enables you and your Partner to transfer the case to the *Resolved* status.

## Prerequisites
A new created Case on the CloudBlue Connect platform.
The system also allows transfering Inquiring Cases to the Pending state once all required data is presented.

## Transferable statuses
Once the issue or problem is fixed, the system assigns the [Resolved](s-c-resolved.html) status to Pending Cases.
If more information or details required, the system assigns the [Inquiring](s-b-inquiring.html status to your Cases.

## Associated transitions
* [New Case Creation](t-1-new-pending.html)
* [Data Inquiry](t-2-pend-inquiring.html)
* [Inquired Data is Submitted](t-3-inq-pending.html)
* [Case Resolution](t-4-pend-resolved.html)
* [Case Reopening](t-6-res-pending.html)
