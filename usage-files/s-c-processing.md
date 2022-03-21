# Processing Status 
## Description
The *Processing* state is displayed once your spreadsheet file is uploaded to the Connect platform. Thus, this status indicates that the system starts processing your usage report file. In case the system successfully process your uploaded spreadsheet file, the usage file object is assigned to the *Ready* status. If the system cannot process your file due to invalid data format or any other error, your usage file object is transferred to the *Invalid* state.
## Prerequisites
A usage file object in the [Uploading](s-b-uploading.html) state.
## Transferable statuses
Once your uploaded spreadsheet is processed successfully, the system assigns the [Ready](s-e-ready.html) status to the usage file object.
Otherwise, the file processing is failed and the system transfers the usage file object to the [Invalid](s-d-invalid.html) state.
## Associated transitions
* [Usage File Processing](t-3-upl-processing.html)
* [File is Processed](t-6-pro-ready.html)
