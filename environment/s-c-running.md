# Running Status 
## Description
Once your environment is successfully deployed in the *Cloud* mode, the system assigns the *Running* status to this environment. In general, it is required to specify a git repository with your extension and a version tag for deploying such environments. Therefore, your extension will be available and will be running in the Cloud. 

The system will display task metrics (timing, processing, and total) and will also provide event logs for your deployed environment. Environment variables, tasks queues, and schedules can also be managed once this environment is assigned to the *Running* state,

Note that the system doesn't allow removing extensions on the CloudBlue Connect platform in case at least one of your environments has this status.

## Prerequisites
An environment object in the [Deploying](s-b-deploying.html) state and a Git repository with your extension are required.

# Transferable statuses
In case you stop your running environment, it is assigned to the [Stopping](s-d-stopping.html) state.

## Associated transitions
* [Cloud Environment Launch](t-3-deploy-running.html)
* [Stopping Cloud Environment](t-4-running-stopping.html)

