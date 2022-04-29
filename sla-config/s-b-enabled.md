# Enabled Status
## Description
Once SLA settings are enabled, the system transfers the settings object to the *Enabled* state. This status indicates that provided configuration is applied to your selected Connect object. Therefore, the system will automatically assign each object that is associated with the SLM functionality to the corresponding SLO zone according to provided configuration.  
It is also possible to change your provided settings and restore default parameters if necessary.
## Prerequisites
SLA settings with the [Disabled](s-a-disabled.html) status.
## Transferable statuses
The system allows deactivating provided configuration and consequently assign SLA settings to the [Disabled](s-a-disabled.html) state.
## Associated transitions
* [SLA Settings Activation](t-1-dis-enabled.html)
* [SLA Settings Dectivation](t-2-enab-disabled.html)
