# Invalid Status 
## Description
The Invalid status indicates that your uploaded spreadsheet file contains invalid data or it is missing required information. In case the system assigns this status to your usage file object, you can download your processed file to view provided errors and issues with your specified data.

Note that once the system transfers your usage report file to the Invalid state, it is necessary to fix all issues and upload your spreadsheet file once again. Thereafter, the system assigns your usage file object back to the Uploading state.

It is also highly recommended to familiarize yourself with the required data format and provided usage file examples within the [Usage – Vendor Portal](https://connect.cloudblue.com/community/modules/usage_module/vendor-portal/) documentation.

## Prerequisites
Invalid usage file in the [Processing](s-c-processing.html) state.
## Transferable statuses
Once Vendors fix all provided errors and reupload their spreadsheet file, the system assigns the usage file object to the [Uploading](s-b-uploading.html) status.
Note that Vendors can also delete their invalid usage file object.
## Associated transitions
* [Processing Failure](t-4-pro-invalid.html)
* [Invalid File Reuploading](t-5-inv-uploading.html)

