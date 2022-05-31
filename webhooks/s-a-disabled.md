# Disabled Status
## Description
The *Disabled* status implies that your webhook is switched off and it will not provide any HTTP callbacks. This status can be assigned to a new webhook object in case the corresponding option is selected. Once your enabled webhook is turned off, the system also assigns the *Disabled* status to your webhook.  
Disabled webhooks can be enabled or removed if necessary.
## Prerequisites 
A new webhook object with the selected **Disabled** option.  
Alternatively, a webhook object in the [Enabled](s-b-enabled.html) state that should be deactivated.
## Transferable statuses
Once your webhook is successfully activated, it is assigned to the [Enabled](s-b-enabled.html) state.
## Associated transitions
* [Webhook Creation](t-1-new-disabled.html)
* [Webhook Activation](t-2-dis-enabled.html)
* [Webhook Deactivation](t-3-enab-disabled.html)
* [Disabled Webhook Removal](t-5-dis-deleted.html)
