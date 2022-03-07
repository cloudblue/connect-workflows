# Accepted Status 
## Description
Once Distributors or Resellers accept usage file object, the system automatically transfers provided usage record objects to the *Accepted* state. Thereafter, Distributors or Resellers can use presented usage record data for subsequent billing operations. 

In case all required billing operations are accomplished, the usage file object can be successfully closed by Distributors or Resellers. Consequently, the system assigns the *Closed* status to all associated usage records.
## Prerequisites
Accepted usage record object in the [Pending](s-d-pending.html) state.
## Transferable statuses
Once Distributors or Resellers provide the *extarnal billing id* and *extarnal billing note* data next to the submitted usage record object, the system transfers this object to the [Closed](s-g-closed.html) state.
## Associated transitions
* [Record Acceptance](t-8-pend-accepted.html)
* [Record Closure](t-9-acc-closed.html)