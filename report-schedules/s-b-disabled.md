# Disabled Status
## Description
In case Connect users decide to turn off their enabled report schedule object, the system assigns this object to the *Disabled* status. Therefore, report objects and their corresponding report files will not be generated on the Connect platform. 
Connect users can also turn on their disabled report schedules if necessary. Note that the systm also allows deleting disabled report schedule objects.

## Prerequisites
A report schedule object with the [Enabled](s-a-enabled.html) status.
## Transferable statuses
Once Connect users switch on their disabled report schedule object, the system transfers this object back to the [Enabled](s-a-enabled.html) state.
Disabled report schedules can also be permanently deleted.
## Associated transitions
* [Schedule Deactivation](t-2-enabled-disabled.html)
* [Schedule Reactivation](t-3-disabled-enabled.html)
* [Disabled Schedule Removal](t-5-disabled-deleted.html)
