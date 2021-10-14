# Usage Files
## Overview
Usage files represent uploaded spreadsheets that are required to work with the Usage module on the CloudBlue Connect platform. Usage files include information on consumed services and can feature pricing details for the subsequent billing operations. In addition, note that uploaded usage files should contain data that is used to identify your product, defined items, and your generated subscription.
Note that Vendors are required to create a usage file object on Connect before uploading their spreadsheet file. Once a new object is created, the system transfers this object to the *Draft* state. Thereafter, Vendors can upload their spreadsheet via the generated usage file object. In case the uploaded spreadsheet file contains any errors, the system assigns the *Invalid* status to the usage file object. Otherwise, the system successfully processes the provided spreadsheet, and the usage file object is assigned to the *Ready* state.
Once Vendors submit the usage file object to their business partners, the system allows Distributors or Resellers to accept or reject the usage file and assign the corresponding state to the object.
In case the usage file is approved, Distributors and Resellers can launch all required billing operations. Once all billing operations are accomplished, the system allows Distributors or Resellers to close usage file and transfer the object to the corresponding state.

## Report Statuses
The following list displays available usage file statuses on the CloudBlue Connect platform. Select a status from the provided diagram or click on a contextual link below to display detailed status information:

* A. [Draft](s-a-draft.html)
* B. [Uploading](s-b-uploading.html)
* C. [Processing](s-c-processing.html)
* D. [Invalid](s-d-invalid.html)
* E. [Ready](s-e-ready.html)
* F. [Pending](s-f-pending.html)
* G. [Rejected](s-g-rejected.html)
* H. [Accepted](s-h-accepted.html)
* I. [Closed](s-i-closed.html)

## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [Usage File Creation](t-1-new-draft.html)
2. [Usage File Uploading](t-2-draft-uploading.html)
3. [Usage File Processing](t-3-upl-processing.html)
4. [Processing Failure](t-4-pro-invalid.html)
5. [Invalid File Reuploading](t-5-inv-uploading.html)
6. [File is Processed](t-6-pro-ready.html)
7. [Processed File Reuploading](t-7-ready-uploading.html)
8. [File is Submitted](t-8-ready-pending.html)
9. [Pending File Rejection](t-9-pend-rejected.html)
10. [Rejected File Reuploading](t-10-reject-uploading.html)
11. [Usage File Acceptance](t-11-pend-accepted.html)
12. [Usage File Closure](t-12-accept-closed.html)

## Learn more
Refer to the [Connect community page](https://connect.cloudblue.com/community/modules/usage/) for more information.
