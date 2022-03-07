# Accepted Status 
## Description
The *Accepted* status, as its name suggest, indicates that Distributors or Resellers reviewed and accepted the provided usage report file. Therefore, the accepted file and provided usage information can be used for subsequent billing operations.
Once all billing operations are accomplished, the system requires Distributors or Resellers to upload a usage file with external billing id and external billing note for each provided usage record. Alternatively, the system allows specifying such information for all provided records via the Extract tab. In case all required information is presented, the system assigns the *Closed *status to the usage file object.
## Prerequisites
A usage file object in the [Pending](s-f-pending.html) state.
## Transferable statuses
Once Distributors or Resellers close the provided usage file, the system assigns the [Closed](s-i-closed.html) status to the usage file object.
## Associated transitions
* [Usage File Acceptance](t-11-pend-accepted.html)
* [Usage File Closure](t-12-accept-closed.html)
