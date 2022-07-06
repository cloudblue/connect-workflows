# Deploying Status
## Description
The *Deploying* status indicates that the system is currently processing your environment object. This status is automatically assigned in case you start to deploy your *local* or *cloud* environment. Once the platform finishes to process the required environment object, this object will be assigned to one of multiple statuses depending on the selected mode or occurred errors.

Note that the system does not allow removing or editing your services that include at least one environment in the *Deploying* state. 

## Prerequisites 
An environment object with one of the following statuses is required:
* [Uninitialized](s-a-uninitialized.html)
* [Stopped](s-e-stopped.html)
* [Disconnected](s-g-disconnected.html)
* [Errored](s-h-errored.html)

## Transferable statuses
Once your *local* environment is deployed successfully, this envrionment is assigned to the [Connected](s-f-connected.html) state.
When a cloud environment is deployed, this environment is transferred to the [Running](s-c-running.html) status.
In case of an error, your environment object is assigned to the [Errored](s-h-errored.html)

## Associated transitions
* [Environment Deployment](t-2-uninit-deploying.html)
* [Cloud Environment Launch](t-3-deploy-running.html)
* [Cloud Environment Restart](t-6-stopped-deploying.html)
* [Local Environment Connection](t-7-deploy-connected.html)
* [Local Environment Reconnection](t-9-disco-deploying.html)
* [Local Environment Switch](t-10-disco-deploying.html)
* [Environment Launch Error](t-11-deploy-errored.html)
* [Environment Relaunch](t-12-error-deploying.html)
