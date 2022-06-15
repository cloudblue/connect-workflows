# Active Status 
## Description
The system assigns the *Active* status to your price list version once it is successfully activated according to your provided schedule. This status is also assigned in case your price list version is activated manually. In general, the *Active* status implies that your current version is being used for price list exchange operations for a particular product. 

Note that only one version can be activated for a single price list. Therefore, when a new version is activated, your active previous version will be assigned to the *Expired* state. 
## Prerequisites
A price list version object in the [Draft](s-b-draft.html) state or in the [Scheduled](s-d-scheduled.html) state.
## Associated transitions
* [Version Activation](t-3-draft-active.html)
* [Scheduled Version Activation](t-6-scheduled-active.html)
* [Version Expiration](t-7-active-expired.html)
