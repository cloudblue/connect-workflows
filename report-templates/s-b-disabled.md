# Disabled Status 
## Description
The system allows disabling report templates that should be hidden from your account users. Therefore, in case your report template is assigned to the *Disabled* status, this template cannot be selected to generate a report file on the Connect platform. The system also prompts you to provide a note before disabling your report template.

Note that the system blocks disabled report templates in case its associated report repository is assigned to the *Failed* status.
## Prerequisites
Report template in the [Enabled](s-a-enabled.html) state.
## Transferable statuses
Once your report template is reactivated, the system assigns the [Enabled](s-a-enabled.html) status to this template.  
In case your report repository with your disabled report template is transferred to the *Failed* state, the system assigns the [Blocked](s-c-blocked.html) status to this template.
## Associated transitions
* [Template Deactivation](t-2-enabled-disabled.html)
* [Template Reactivation](t-3-disabled-enabled.html)
* [Template is Blocked](t-4-enabled-disabled-blocked.html)
* [Template is Unblocked](t-5-blocked-enabled.html)
