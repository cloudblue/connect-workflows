# Pending Status 
## Description
The *Pending* status of a usage file object indicates the Vendors successfully submitted a usage file to Distributors or Resellers. Thus, the system enables Distributors or Resellers to download and review the provided spreadsheet file.

In case of an error, Distributors or Resellers can reject the usage file. In this case, the system automatically transfers the usage file object to the *Rejected* state. Thereafter, Vendors are required to fix the issue and upload the spreadsheet file once again.

Otherwise, Distributors or Resellers can accept the provided usage file. Therefore, the system assigns the *Accepted* status to the usage file object.
## Prerequisites
A usage file object in the [Ready](s-e-ready.html) state.
## Transferable statuses
The system allows rejecting usage file objects in case of an error and transfer the object to the [Rejected](s-g-rejected.html) state.
Otherwise, usage file object can be accepted and assigned to the [Accepted](s-h-accepted.html) status.

## Associated transitions
* [File is Submitted](t-8-ready-pending.html)
* [Pending File Rejection](t-9-pend-rejected.html)
