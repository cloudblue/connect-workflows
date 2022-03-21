# Active Status
## Description
Once Distributors create a new agreement and check the **Activate Version** checkbox, the system generates a new agreement version object and transfers it to the *Active* state. Alternatively, Connect allows Distributors to manually activate agreement versions that are assigned to the *Inactive* status. Therefore, the *Active* status indicates that Distributors decided to use their selected version object as an actual template for their subsequent contracts. The system will also generate contracts based on the active agreement version.
Note that Distributors can also deactivate their agreement versions. In this case, the system transfers the version object to the *Inactive* state.
## Prerequisites
A new created agreement with checked **Activate Version** checkbox or a version object in the [Inactive](s-b-inactive.html) state required.
## Transferable statuses
In case a version object is deactivated, the system assigns this object to the [Inactive](s-b-inactive.html) status.
## Associated transitions
* [New Active Agreement Version Creation](t-1-new-active.html)
* [New Inactive Agreement Version Creation](t-2-new-inactive.html)
* [Agreement Version Deactivation](t-3-act-inactive.html)
* [Agreement Version Reactivation](t-4-inact-active.html)
* [Active Agreement Version Removal](t-5-act-deleted.html)
