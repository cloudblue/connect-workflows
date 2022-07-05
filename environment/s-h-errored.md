# Errored Status 
## Description
The *Errored* status implies that the system cannot process your configured *cloud* environment. Therefore, the system typically returns a corresponding error and your extension cannot be launched within this errored environment. 

In general, it is recommended to make sure that your specified Git URL is valid and includes your correct release tag. Furthermore, make sure that your authorization credentials are correct in case you are using a private Git repository.

## Prerequisites
An environment object the [Deploying](s-b-deploying.html) state that cannot be processed by the system.

# Transferable statuses
In case you relaunch your *errored* environment, it is assigned back to the [Deploying](s-b-deploying.html) state.
The system allows switching your environment object to the *Cloud* mode and thus assign the [Disconnected](s-g-disconnected.html) state to this object.

## Associated transitions
* [Environment Launch Error](t-11-deploy-errored.html)
* [Environment Relaunch](t-12-error-deploying.html)
* [Errored Environment Switch](t-13-error-disconnected.html)
