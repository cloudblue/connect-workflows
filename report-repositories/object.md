# Report Repositories
## Description
CloudBlue Connect allows adding and managing your Git repositories that are used to define your custom report templates. Therefore, added report templates enable Connect users to generate custom report files that contain required Connect data. 
Once Connect users add their Git repository with custom report templates, the system creates a repository object and assigns the *Configuring* status to this object. 
In case the system successfully processes the added repository, its corresponding object is automatically transferred to the *Ready* state. Otherwise, the system fails to process your added repository and assigns the *Failed* status to the repository object.
Connect users can edit or update their report repositories with the *Failed* and *Ready* statuses. Note that the system also allows deleting repositories in the *Failed* state.

## Available Statuses
The following list contains available statuses for the report repository objects on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:

* A. [Configuring](s-a-configuring.html)
* B. [Ready](s-b-ready.html)
* C. [Failed](s-c-failed.html)

## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [New Repository Object Creation](t-1-new-configuring.html)
2. [Successful Repository Configuration](t-2-conf-ready.html)
3. [Repository Processing Failure](t-3-conf-failed.html)
4. [Repository Details Edit](t-4-fail-configuring.html)
5. [Repository Removal](t-5-fail-deleted.html)
6. [Repository Update](t-6-ready-configuring.html)


## Learn more
Refer to the [Account module documentation](https://connect.cloudblue.com/community/modules/account/reports/) from the Connect Community page for more information.
