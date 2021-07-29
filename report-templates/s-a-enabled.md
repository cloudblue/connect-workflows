# Enabled Status 
## Description
The *Enabled* report template state indicates that this template is available for your account users. Therefore, the system can generate a report file by using your enabled report template. The system prompts your account users to select enabled templates from the provided list while creating a new report or report schedule.
Enabled report templates can be disabled and consequently hidden from users. In addition, note that the system blocks enabled report templates in case their associated report repository is assigned to the *Failed* status.
## Prerequisites
An added report repository that includes your report template is required to assign this template to the *Enabled* state.
Moreover, the system transfers your reactivated templates to this state from the [Disabled](s-b-disabled.html) and [Blocked](s-c-blocked.html) statuses.
## Transferable statuses
Enabled report templates can be assigned to the [Disabled](s-b-disabled.html) status.
Furthermore, the system transfers enabled templates to the [Blocked](s-c-blocked.html) state in case it is no longer available within its corresponding repository.
## Associated transitions
* [New Template Addition](t-1-new-enabled.html)
* [Template Concealment](t-2-enabled-disabled.html)
* [Template Reactivation](t-3-disabled-enabled.html)
* [Template is Blocked](t-4-enabled-disabled-blocked.html)
* [Template is Unblocked](t-5-blocked-enabled.html)

