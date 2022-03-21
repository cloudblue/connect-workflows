# Configuring Status
## Description
Once a new repository object is created on the Connect platform, the system assigns the *Configuring* status to this object. In addition, the system uses this status if processed or failed report repository objects are edited or updated by Connect users.
Therefore, the *Configuring* status indicates that the system processes added or updated/edited report repository.

## Prerequisites 
A new added report repository is required. Furthermore, the system starts configuring edited repositories in the [Ready](s-b-ready.html) or [Failed](s-c-failed.html) states.
## Transferable statuses
In case the system successfully processes an added or updated/edited report repository, its corresponding object is automatically assigned to the [Ready](s-b-ready.html) status.
Otherwise, the system transfers the repository object to the [Failed](s-c-failed.html) state.
## Associated transitions
* [New Repository Object Creation](t-1-new-configuring.html)
* [Successful Repository Configuration](t-2-conf-ready.html)
* [Repository Processing Failure](t-3-conf-failed.html)
* [Repository Details Edit](t-4-fail-configuring.html)
* [Repository Update](t-6-ready-configuring.html)

