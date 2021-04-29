# Draft Status
## Description
Once Vendors create a new price list on the Connect platform, the system assigns the *Draft* status to this created price list.
A draft list can be deleted or activated by Vendors. Thus, the system will transfer this list to the corresponding state.
Note that Vendor can also schedule price list activation. In this case, the system assigns the *Scheduled* state. If Vendors 
## Prerequisites 
A defined product and a specified marketplace on the CloudBlue Connect platform.
## Transferable statuses
Once a Vendor activates a price list, the sytem assigns the [Active](s-c-active.html) status to this list.
In case a Vendor schedules the price list activation, the system transfers the list to the [Scheduled](s-b-scheduled.html) state.
Note that Vendors can also delete draft lists.
## Associated transitions
* [Draft Creation](t-1-new-draft.html)
* [Price List Schedule](t-2-draft-scheduled.html)
* [Schedule Cancellation](t-3-schedule-draft.html)
* [Draft Activation](t-5-draft-active.html)
* [Draft Removal](t-7-draft-deleted.html)