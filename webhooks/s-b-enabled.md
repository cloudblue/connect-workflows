# Enabled Status
## Description
The *Enabled* status indicates that your webhook is switched on. Therefore, your webhook will provide required HTTP callbacks for your specified events within the system. This status can be assigned to a new webhook object in case the **Enabled** switch is activated. In case disabled webhooks are activated, the system also assigns the *Enabled* status to such webhook.  
Enabled webhooks can be deactivated or deleted if necessary.
## Prerequisites 
A new webhook object with the selected **Enabled** option.  
Alternatively, a webhook object in the [Enabled](s-b-enabled.html) state that should be deactivated.
## Transferable statuses
Once your webhook is successfully activated, it is assigned to the [Enabled](s-b-enabled.html) state.
## Associated transitions
* [Webhook Creation](t-1-new-disabled.html)
* [Webhook Activation](t-2-dis-enabled.html)
* [Webhook Deactivation](t-3-enab-disabled.html)
* [Disabled Webhook Removal](t-5-dis-deleted.html)

