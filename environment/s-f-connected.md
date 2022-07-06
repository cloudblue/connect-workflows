# Connected Status 
## Description
The *Connected* status implies that your environment is successfully deployed in the *Local* mode. To deploy such an environment, it is typically required to use Connect CLI tool to bootstrap your extension project and then launch it. Thus, your extension will be available within your configured *local* environment.

The system will display task metrics (timing, processing, and total) for your deployed environment. The system also allows managing environment variables, tasks queues, and schedules once your environment is transferred to the *Connected* state.

Note that the system doesn't allow removing extensions on the CloudBlue Connect platform in case at least one of your environments is assigned this status.
## Prerequisites
An environment object in the [Deploying](s-b-deploying.html) state and your configured extension project are required.

# Transferable statuses
In case you disconnect your local environment, it is assigned to the corresponding [Disconnected](s-g-disconnected.html) state.

## Associated transitions
* [Local Environment Connection](t-7-deploy-connected.html)
* [Local Environment Disconnection](t-8-connected-disconnected.html)
