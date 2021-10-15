# Uploading Status
## Description
Once Vendors successfully upload a new usage file, each specified usage record is automatically generates a corresponding object on the Connect platform. The system also automatically assigns your generated usage record objects to the *Uploaded* state. Therefore, this status indicates that usage record objects are uploaded successfully. 

This status also indicates that the system also processing and validating provided usage record objects. In case your provided usage record is successfully validated, the system automatically assigns it to the *Validated* status. 

Otherwise, your provided usage record can include invalid data or any other error. In this case, the system assigns such usage records to the *Invalid* state. 
## Prerequisites 
A new uploaded usage record on the Connect platform.
## Transferable statuses
Once the system successfully processes and validates the provided usage record, it is automatically assigned to the [Validated](s-b-validated.html) status.
In case the system cannot process the provided usage record, it is transferred to the [Invalid](s-c-invalid.html) state.
## Associated transitions
* [New Record Creation](t-1-new-uploaded.html)
* [Record Validation](t-2-upl-validated.html)
* [Failed Record Processing](t-3-upl-invalid.html)
* [Record Reuploading](t-4-inv-uploaded.html)
* [Rejected Record Reuploading](t-7-rej-uploaded.html)
