# Processing Status
## Description
Once a new tier configuration instance is generated or successfully validated, the system assigns the *Processing* status to this instance. Alternatively, this status indicates that an active tier configuration was updated by Vendors or Distributors. Therefore, Vendors are required to process this tier configuration by approving or rejecting its corresponding tier configuration request.

## Prerequisites
Any **Tier-scope** parameter and new subscriptions are required to generate processing tier configs.
Furthermore, once a draft tier config is successfully validated, the system assigns the *Processing* status to the tier config.
## Transferable statuses
Once Vendors appoves a tier request, its corresponding tier configuration is assigned to the [Active](s-c-active.html) state by the system
## Associated transitions
* [New Processing Config](t-1-new-processing.html)
* [Draft Config Validation](t-3-draft-processing.html)
* [Config Activation](t-5-pro-active.html)
* [Config Update](t-6-act-processing.html)
