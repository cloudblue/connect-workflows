# Draft Status
## Description
Once your version is created and successfully processed by the system, it is automatically assigned to the *Draft* status. Therefore, this represents an inactive object state that allows editing required parameters of your price list version.  

The system allows scheduling the activation of your draft price list and allows activating your draft price list versions manually. Draft price list versions can also be removed if necessary.

## Prerequisites 
A price list version in the [Pending](s-a-pending.html) state.
## Transferable statuses
Once your draft version object is activated, the system transfers this object to the [Active](s-c-active.html) state.
In case the activation of your price list version is scheduled, the system assigns the [Scheduled](s-d-scheduled.html) status to this object.

## Associated transitions
* [Draft Processing](t-2-pend-draft.html)
* [Version Activation](t-3-draft-active.html)
* [Activation is Scheduled](t-4-draft-scheduled.html)
* [Activation is Unscheduled](t-5-scheduled-draft.html)
* [Draft Removal](t-8-draft-deleted.html)
