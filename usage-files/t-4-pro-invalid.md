# Processing Failure
## Description
This transition indicates that the system failed to process the provided spreadsheet file due to wrong data format or any other error. Therefore, the system transfers the usage file object to the [Invalid](s-d-invalid.html) state. It is highly recommended to familiarize yourself with the provided data format in the [Usage module - Vendor Portal](https://connect.cloudblue.com/community/modules/usage_module/vendor-portal/) documentation.
## Prerequisites
A usage file object in the [Processing](s-c-processing.html) state.
## Operation results
A usage file object with the [Invalid](s-d-invalid.html) status.