# Webhook Objects
## Overview
Webhooks represent objects on CloudBlue Connect that allow platform users to define HTTP callbacks. Such callbacks are triggered by your selected event within the system. Namely, your defined webhook can be triggered if your request or usage file queue is changed, in case your draft or inquiring requests require validation, and so on. Once your specified event is occurred, the webhook sends corresponding *GET* or *POST* request to your provided endpoint URL. Therefore, webhooks can drastically facilitate the communication between the Connect platform and any web application that can accept HTTP requests.

It is also important to note that your webhooks on the Connect platform can also include headers with your provided *keys* with *values* and arbitrary JSON object that is appended to your token as the *.data* property.
## Learn more
Refer to the [Webhooks documentation](https://connect.cloudblue.com/community/modules/extensions/webhooks/) to learn how to create and manage your webhooks.
[Dynamic Parameters Validation use case](https://connect.cloudblue.com/community/modules/extensions/webhooks/) provides an example of a webhook that is used for pre-provisioning request validaiton.
