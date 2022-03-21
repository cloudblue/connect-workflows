# Draft Status
## Description
Once a new usage file object is created, the system automatically assigns the Draft status to this object. Thus, this status indicates that it is necessary to upload a spreadsheet file with your specified data. The system provides a template before and after your usage file object is created. Thereafter, it is necessary to fill out your acquired template or create a new spreadsheet with your usage report information. Refer to the [Usage – Vendor Portal](https://connect.cloudblue.com/community/modules/usage_module/vendor-portal/#Populating_Usage_File) documentation to learn more about populating your file with required usage report data.

Note that once Vendors upload their spreadsheet file, the system transfers a draft usage file object to the Uploading state.
## Prerequisites 
A new created usage file object on the CloudBlue Connect platform.
## Transferable statuses
Once Vendors upload their spreadsheet file, the system assigns the [Uploading](s-b-uploading.html) status to the usage file object.
Note that draft usage file objects can also be removed if necessary.
## Associated transitions
* [Usage File Creation](t-1-new-draft.html)
* [Usage File Uploading](t-2-draft-uploading.html)
