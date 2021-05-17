# Draft Status
## Description
The system assigns the *Draft* status to a new tier configuration instance in case the dynamic validation capability is enabled. Thus, the Connect platform enables Distributors implement the real-time validation of tier configuration requests. Once a tier request is successfully validated, the system transfers this configuration to the *Processing* state. Otherwise, this draft tier configuration is permanently deleted.
## Prerequisites
Enabled **Dynamic Validation – Tier Config Request – Draft** product capability, any **Tier-scope** parameter, and new subscriptions are required to generate draft tier configs.
## Transferable statuses
Tier configs are transferred to the [Processing](s-b-processing.html) status in case their corresponding requests are successfully validated.
## Associated transitions
* [Draft Config Creation](t-2-new-draft.html)
* [Draft Config Validation](t-3-draft-processing.html)
* [Draft Config Removal](t-4-draft-deleted.html)