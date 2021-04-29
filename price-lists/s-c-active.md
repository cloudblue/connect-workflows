# Active Status 
## Description
The system assigns the *Active* status to a created price list once Vendors decide to activate their draft list.
Alternatively, the system assigns this status to a *scheduled* price list in case Vendors select specific time for price list activation.
Note that Vendors can terminate an active price list. Therefore, the system transfers this price list to the *Terminated* state.
## Prerequisites
A price list in [Draft](s-a-draft.html) or [Scheduled](s-b-scheduled.html) state.
## Associated transitions
* [Scheduled Pricing Activation](t-4-schedule-active.html)
* [Draft Activation](t-5-draft-active.html)
* [Price List Termination](t-6-active-terminated.html)