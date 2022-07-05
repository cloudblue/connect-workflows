# Disconnected Status 
## Description
The *Disconnected* status indicates that your *local* environment is disconnected from the Connect platform. This status is also displayed in case you switch your *cloud* environment to the *Local* mode. Therefore, your *local* environment cannot be used to connect your required extension.

Environment objects in this state can be reconnected by performing the corresponding or switched to the *Cloud* mode if necessary. 

## Prerequisites
An environment object with one of the following statuses is required:
* [Connected](s-f-connected.html)
* [Stopped](s-e-stopped.html)
* [Errored](s-h-errored.html)

# Transferable statuses
In case your environment is reconnected or switched to the *Cloud* mode, it is assigned to the [Deploying](s-b-deploying.html) state.

## Associated transitions
* [Local Environment Disconnection](t-8-connected-disconnected.html)
* [Local Environment Reconnection](t-9-disco-deploying.html)
* [Local Environment Switch](t-10-disco-deploying.html)
* [Errored Environment Switch](t-13-error-disconnected.html)
* [Cloud Environment Switch](t-14-stopped-disconnected.html)
