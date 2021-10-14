# Ready Status 
## Description
In case the system successfully process your uploaded spreadsheet file, your usage file object is transferred to the *Ready* state. Namely, this status indicates that your provided usage report can be submitted to your business partners on the Connect platform.
Once Vendors decide to submit a usage report file to their Distributors or Resellers, the system assigns the *Pending* status to the usage file object. Therefore, your business will be able to review your submitted data. Note that the system also allows reuploading your usage file in case of an error or if your processed file is no longer relevant.
## Prerequisites
A usage file object with the [Processing](s-c-processing.html) status.
## Transferable statuses
In case Vendors submit a usage file to Distributors or Resellers, the system transfers this usage file object to the [Pending](s-f-pending.html) state.
Alternatively, Vendors can reupload their spreadsheet file and assign the [Uploading](s-b-uploading.html) status to the usage file object.
Note that Vendors can also delete their usage file object in this state.
## Associated transitions
* [File is Processed](t-6-pro-ready.html)
* [Processed File Reuploading](t-7-ready-uploading.html)
