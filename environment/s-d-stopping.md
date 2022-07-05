# Stopping Status 
## Description
In case you stop your *cloud* environment, the system assigns the *Stopping* status to this environment. Therefore, this status indicates that the system is stopping your running environment. Once the system successfully stops your environment object, this object will be assigned to the following state.

Note that the system doesn't allow removing extensions on the CloudBlue Connect platform in case at least one of your environments is assigned to the *Stopping* status.

## Prerequisites
An envrionment object in the [Running](s-c-running.html) state is required.

# Transferable statuses
Once the system stops your environment, it is assigned to the [Stopped](s-e-stopped.html) state.

## Associated transitions
* [Stopping Cloud Environment](t-4-running-stopping.html)
* [Cloud Environment is Stopped](t-5-stopping-stopped.html)
