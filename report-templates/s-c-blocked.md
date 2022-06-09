# Blocked Status 
## Description
In case your repository with your custom report templates is assigned to the *Failed* status, the system transfers your added templates to the *Blocked* state. Such report templates cannot be used to generate reports on Connect.

Blocked report templates can be enabled again once their associated report repository is assigned to the *Ready* status, and this repository includes required templates. 
In addition, the system automatically deletes blocked report templates in case their corresponding repository is removed from the Connect platform.
## Prerequisites
The system blocks your report templates with [Disabled](s-b-disabled.html) and [Enabled](s-a-enabled.html) statuses in case their repository is transfered to the *Failed* state.
## Transferable statuses
Once your report repository is assigned to the *Ready* status, the system transfers your blocked report template back to the [Enabled](s-a-enabled.html) state.  
If your *failed* repository is deleted, the system removes your blocked templates.
## Associated transitions
* [Template is Blocked](t-4-enabled-disabled-blocked.html)
* [Template is Unblocked](t-5-blocked-enabled.html)
* [Template Removal](t-6-blocked-deleted.html)
