# Enabled Status
## Description
The *Enabled* status indicates that your webhook is switched on. Therefore, your webhook will provide required HTTP callbacks for your specified events within the system. This status can be assigned to a new webhook object in case the **Enabled** switch is activated. In case disabled webhooks are activated, the system also assigns the *Enabled* status to such webhook.  
Enabled webhooks can be deactivated or deleted if necessary.
## Prerequisites 
A new webhook object with the selected **Enabled** option.  
Alternatively, a webhook object in the [Disabled](s-a-disabled.html) state that should be activated.
## Transferable statuses
In case your webhook is deactivated, the system assigns it to the [Disabled](s-a-disabled.html) state.
## Associated transitions
* [Webhook Activation](t-2-dis-enabled.html)
* [Webhook Deactivation](t-3-enab-disabled.html)
* [Enabled Webhook Creation](t-4-new-enabled.html)
* [Enabled Webhook Removal](t-6-dis-deleted.html)
