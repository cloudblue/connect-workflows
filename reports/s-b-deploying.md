# Deploying Status
## Description
The *Deploying* report status indicates that a new report is being deployed on the Connect platform. From this particular state, the system decides if a report file is generated successfully. Thereafter, in case the report creation is successful, the system assigns the *Ready* status to this report. Otherwise, the report creation is failed and the system assigns the corresponding status to it.
## Prerequisites 
A new generating report with the [Pending](s-a-pending.html) status.
## Transferable statuses
Once a report is successfully created, it is transferred to the [Ready](s-c-ready.html) state.
In case of an error, this report is converted to the [Failed](s-d-failed.html) state.
## Associated transitions
* [New Report Deployment](t-2-pen-deploying.html)
* [Report Creation Success](t-3-dep-ready.html)
* [Report Creation Failure](t-4-dep-failed.html)
