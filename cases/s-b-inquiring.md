# Inquiring Status
## Description
The system allows inquiring information or details that are required to address the issue or request from a pending Case. Therefore, the Case is assigned to the *Inquiring* status and the system requires to provide necessary data or details.
The Case is transferred back to the *Pending* state if required information is submitted. Note that the system allows both Case reporters and Case assignees to submit data and trasnfer their Case to the *Pending* state.
## Prerequisites
Helpdesk Cases with the [Pending](s-a-pending.html) status.
## Transferable statuses
Once all required data is submitted, the system transfers Cases to the [Pending](s-a-pending.html) state.
## Associated transitions
* [Data Inquiry](t-2-pend-inquiring.html)
* [Inquired Data is Submitted](t-3-inq-pending.html)
