# Usage Files
## Overview
Usage files represent uploaded spreadsheets that are required to work with the Usage module on the CloudBlue Connect platform. Usage files include information on consumed services and can feature pricing details for the subsequent billing operations. In addition, note that uploaded usage files should contain data that is used to identify your product, defined items, and your generated subscription.
Note that Vendors are required to create a usage file object on Connect before uploading their spreadsheet file. Once a new object is created, the system transfers this object to the *Draft* state. Thereafter, Vendors can upload their spreadsheet via the generated usage file object. In case the uploaded spreadsheet file contains any errors, the system assigns the *Invalid* status to the usage file object. Otherwise, the system successfully processes the provided spreadsheet, and the usage file object is assigned to the *Ready* state.
Once Vendors submit the usage file object to their business partners, the system allows Distributors or Resellers to accept or reject the usage file and assign the corresponding state to the object.
In case the usage file is approved, Distributors and Resellers can launch all required billing operations. Once all billing operations are accomplished, the system allows Distributors or Resellers to close usage file and transfer the object to the corresponding state.

## Additional Information
Please refer to the [Usage Management Module](https://connect.cloudblue.com/community/modules/usage/) documentation for more information.
