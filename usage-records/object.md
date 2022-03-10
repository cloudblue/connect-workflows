# Usage Records
## Overview
Usage records is your specified data that is associated with your required subscription, purchased items and usage of consumed services. Namely, a usage record represents a single row with information provided by Vendors. Usage records can be found within the **Records** tab of a usage report spreadsheet.
Your usage record workflow is interconnected with the workflow of your provided usage file. Namely, once Vendor upload their spreadsheet file, the system assigns the *Uploaded* status to all provided usage record. In case your usage record includes data in wrong format or any other error, the system assigns the *Invalid* status to this record and usage file. Otherwise, the system transfers the usage record object to the *Validated* state.
Once Vendors submit their usage file to Distributors or Resellers, the system assigns the *Pending* status to the usage file object and each provided usage record object. Distributors or Resellers can accept or reject usage file and consequently assigns corresponding statuses to all usage records. In case usage record is rejected, Vendors can fix the identified issues and reupload usage file with required records once again. In case usage records are accepted, Distributors or Resellers can use this record for their subsequent billing operations. Once all billing operations are accomplished, the system allows Distributors or Resellers close the provided usage file and its usage records. 

## Report Statuses
The following list displays available statuses of usage record objects on the CloudBlue Connect platform. Select a status from the provided diagram or click on a contextual link below to display detailed status information:

* A. [Uploaded](s-a-uploaded.html)
* B. [Validated](s-b-validated.html)
* C. [Invalid](s-c-invalid.html)
* D. [Pending](s-d-pending.html)
* E. [Rejected](s-e-rejected.html)
* F. [Accepted](s-f-accepted.html)
* G. [Closed](s-g-closed.html)

## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [New Record Creation](t-1-new-uploaded.html)
2. [Record Validation](t-2-upl-validated.html)
3. [Failed Record Processing](t-3-upl-invalid.html)
4. [Record Reuploading](t-4-inv-uploaded.html)
5. [Record is Submitted](t-5-val-pending.html)
6. [Record is Rejected](t-6-pend-rejected.html)
7. [Rejected Record Reuploading](t-7-rej-uploaded.html)
8. [Record Acceptance](t-8-pend-accepted.html)
9. [Record Closure](t-9-acc-closed.html)

## Learn more
Refer to the [Connect community page](https://connect.cloudblue.com/community/modules/usage-module/) for more information.
