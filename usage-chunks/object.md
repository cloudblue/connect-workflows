# Usage File Chunks
## Overview
Usage file chunks are generated when your usage files are succussfully uploaded and accepted within the system. Usage file chunks represent objects that include your actual usage record data. Such objects also allow downloading required information by using the API or graphical user interface. In order to get this information, the usage file chunk object should be assigned to the *Ready* status.  

Once usage records are applied for the subsequent billing operations, it is required to assign an external identifier for your usage file chunk object. When your external billing identifer and billing note are specified successfully, the usage file chunk objects will be automatically *closed* by the system.  

In case the system fails to generate a new usage file chunk due a technical problem, it is assigned to the *Failed* state. Such objects do not allow accessing usage record data and cannot be used for the following billing operations.  
## Additional Information
Please refer to the [Usage module](https://connect.cloudblue.com/community/modules/usage_module/) documentation for more information on the usage file management.
