# Enabled Status
## Description
Once a new report schedule is generated on the Connect platform, the system assigns the *Enabled* status to this report. Enabled report schedule objects can be disabled or deleted. Furthermore, in case Connect users decided to turn on their disabled report schedule object, the system also transfers this object to the *Enabled* state.
Enabled report schedules are used to automatically generate required report files based on specified template and schedule triggers.
## Prerequisites
A new created report schedule object or a disabled report schedule required.
## Transferable statuses
Enabled report schedules can be switched off and assigned to the [Disabled](s-b-disabled.html) state.
In addition, the system allows permanently deleting enabled report schedules.
## Associated transitions
* [New Schedule Creation](t-1-new-enabled.html)
* [Schedule Deactivation](t-2-enabled-disabled.html)
* [Schedule Reactivation](t-3-disabled-enabled.html)
* [Enabled Schedule Removal](t-4-enabled-deleted.html)
