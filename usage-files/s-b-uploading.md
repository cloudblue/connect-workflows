# Uploading Status
## Description
The *Uploading* status of a usage file object indicates that Vendors decided to upload their spreadsheet file. Therefore, the system starts uploading the provided usage file. 
Once the usage file is successfully uploaded to the Connect platform, the system transfers the usage file object to the *Processing* state.
## Prerequisites 
A usage file object in one of the following states:

* [Draft](s-a-draft.html) 
* [Invalid](s-d-invalid)
* [Rejected](s-g-rejected)

## Transferable statuses
When your spreadsheet file is uploaded, the system transfers the usage file object to the [Processing](s-c-processing) state.
## Associated transitions
* [Usage File Uploading](t-2-draft-uploading)
* [Usage File Processing](t-3-upl-processing)
* [Invalid File Reuploading](t-5-inv-uploading)
* [Rejected File Reuploading](t-10-reject-uploading)
