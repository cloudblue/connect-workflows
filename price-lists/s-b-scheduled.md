# Scheduled Status
## Description
The Connect platform enables Vendors to schedule a price list activation. In case Vendors set activation time for a draft list, the system assigns the *Scheduled* status to this price list.
Thereafter, the system activates this price list on time that is specified by Vendors. The system also assigns the *Active* status.
Note that Vendors are also able to unschedule this price list. Thus, the system sends its back to the *Draft* state.
## Prerequisites 
A price list in the [Draft](s-a-draft.html) state.
## Transferable statuses
Once a price list is schedules by Vendors, it is transferred to the [Scheduled](s-c-scheduled.html) state.
In case Vendors decide to unschedule this price list, the system converts it back to the [Draft](s-a-draft.html) state.
## Associated transitions
* [Price List Schedule](t-2-draft-scheduled.html)
* [Schedule Cancellation](t-3-schedule-draft.html)
* [Scheduled Pricing Activation](t-4-schedule-active.html)