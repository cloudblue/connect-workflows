# Stopped Status 
## Description
The *Stopped* status, as the name implies, is displayed in case your running *cloud* environment is stopped. Therefore, your extension cannot be used within this environment. The system allows restarting your *cloud* environment or switch it to the *Local* mode if necessary.

## Prerequisites
An environment object in the [Stopping](s-d-stopping.html) state is required.

# Transferable statuses
In case you restart your stopped environment, it is assigned to the the [Deploying](s-b-deploying.html) state.
In case you switch your stopped environment to the *Local* mode, this environment is assigned to the [Disconnected](s-g-disconnected) status.

## Associated transitions
* [Cloud Environment is Stopped](t-5-stopping-stopped.html)
* [Cloud Environment Restart](t-6-stopped-deploying.html)
* [Errored Environment Switch](t-13-error-disconnected.html)
