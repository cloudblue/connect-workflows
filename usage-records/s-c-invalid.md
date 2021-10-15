# Invalid Status 
## Description
The Invalid status is displayed in case your provided usage record contains data in an invalid format or any other error. Note that the system helps Vendors identify invalid usage records by providing the processed usage file with highlighted records in the *Invalid* state.

Once all issues with your usage records are fixed, the system allows reuploading usage file and consequently transfer invalid usage records back to *Uploading* state.
## Prerequisites
The system transfers your [uploaded](s-a-uploaded.html) usage records to the *Invalid* state in case of an error.
## Transferable statuses
In case Vendor fix the identified issues and reupload their usage file, each usage record object is assigned back to the [Uploaded](s-a-uploaded.html) state.
## Associated transitions
* [Failed Record Processing](t-3-upl-invalid.html)
* [Record Reuploading](t-4-inv-uploaded.html)
