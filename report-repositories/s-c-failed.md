# Failed Status 
## Description
The *Failed* repository object status is displayed in case the system fails to process your added repository. Namely, your specified repository and tag might not contain valid report templates. Refer to the [Connect Report SDK documentation](https://connect.cloudblue.com/community/sdk/connect-reports-sdk/) to learn how to create valid report templates for the CloudBlue Connect platform.
The system allows editing repository object details, such as your specified URL and selected tag. Furthermore, note that the system allows removing repository objects only with the *Failed* status.
## Prerequisites
Report repository object in the [Configuring](s-a-configuring.html) state.
## Transferable statuses
Once any of specified repository details are updated or edited, the system assigns the [Configuring](s-a-configuring.html) status to your repository object.
Alternatively, failed report repository objects can be permanently removed from Connect.
## Associated transitions
* [Repository Processing Failure](t-3-conf-failed.html)
* [Repository Details Edit](t-4-fail-configuring.html)
* [Repository Removal](t-5-fail-deleted.html)
