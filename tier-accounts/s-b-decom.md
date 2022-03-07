# Decommissioned Status
## Description
Once your tier account object is removed, the system transfers it to the *Decommissioned* state. Therefore, this status indicates that this object cannot be used to generate new subscriptions or fulfillment requests. 
Tier account objects in the *Decommissioned* state are not visible from the graphical user interface and cannot be returned via corresponding API request. However, the system displays such objects in your previously generated subscriptions and fulfillment request as tier 1, tier 2 or customer accounts.
Furthermore, note that *Decommissioned* tier account objects cannot be restored.
## Prerequisites
A tier account object in the [Active](s-a-active.html) state.
## Associated transition
* [Tier Account Removal](t-2-act-decom.html)
