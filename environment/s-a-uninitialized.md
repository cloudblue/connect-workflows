# Uninitialized Status
## Description
Once a new service is added, the system automatically generates `development`, `staging`, and `production` environment objects and assigns the *Uninitialized* status to these objects. This status indicates that your environments are not configured and not launched yet.

The platform provides *environment identifier* that allows to connect your *local* environment and also allows specifying your Git repository to switch your environment to the *Cloud* mode. Therefore, in case you decide to deploy your environment objects, the system will transfer such objects to the following state.

## Prerequisites 
A new added extension is required.

## Transferable statuses
Once the system starts processing your required environment object, this object is automatically transferred to the [Deploying](s-b-deploying.html) state.

## Associated transitions
* [Environment Creation](t-1-new-uninitialized.html)
* [Environment Deployment](t-2-uninit-deploying.html)
