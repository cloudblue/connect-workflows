# Rejected Status 
## Description
The *Rejected* usage record status indicates that Distributors or Resellers rejected usage file object that features incorrect or outdated usage record data. Therefore, Vendors can fix all identified issues with rejected usage records and reupload usage file once again. In case a usage file is reuploaded, the system automatically transfers associated usage records back to the *Uploaded* state.
## Prerequisites 
Rejected usage record object in the [Pending](s-d-pending.html) state.
## Transferable statuses
Once Vendors decide to reupload the usage file object, each provided usage record is assigned back to the [Uploaded](s-a-uploaded.html) status.
## Associated transitions
* [Record is Rejected](t-6-pend-rejected.html)
* [Rejected Record Reuploading](t-7-rej-uploaded.html)
