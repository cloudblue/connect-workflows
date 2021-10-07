# Draft Request Status
## Description
The Draft request status represent an optional state that is available in case the dynamic validation capability of this request type is enabled. Draft requests and their corresponding draft subscription objects can be used for pre-provisioning validation. 
Once the draft fulfillment request is successfully validated, the system automatically transfers the request to the Pending state. If your validated request requires tier configuration or specifying parameter data, the system automatically transfers this request to corresponding statuses. 
In case a generated draft request is not correct or no longer relevant, the system allows removing such requests.
## Prerequisites
Switch a **Dynamic Validation** capability on to enable the real-time validation of your selected request type.
## Transferable statuses
The draft request can be transferred to one of the following statuses:

* [Tiers Setup](s-c-tiers-setup.html)
* [Inquiring](s-d-inquiring.html)
* [Pending](s-b-pending.html)
## Associated transitions
* [New draft creation](t-2-new-draft.html)
* [Draft to Pending Request Convertion](t-3-draft-pending.html)
* [Draft Request Removal](t-4-draft-deleted.html)
