# Rejected Status 
## Description
In case Distributors or Resellers reject their provided usage report file, the system automatically assigns the *Rejected* status to the usage file object. Thus, this status indicates that Vendors can fix the identified issues and reupload a spreadsheet file. The *Rejected* status can be especially helpful in case wrong or outdated information is presented.
In case Vendors decide to upload the fixed usage report file, the system transfers the usage file object to the *Uploading* state.
## Prerequisites
A usage file object in the [Pending](s-f-pending.html) state.
## Transferable statuses
Once Vendors reupload their rejected usage file, the system assigns the [Uploading](s-b-uploading.html) status to the usage file object.
## Associated transitions
* [Rejected File Reuploading](t-10-reject-uploading.html)
* [Usage File Acceptance](t-11-pend-accepted.html)
