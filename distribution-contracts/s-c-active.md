# Active Status 
## Description
Once a Distributor approves a distribution contract, the system assigns the *Active* status to this contract. Furthermore, the system assigns this status to automatically accepted distribution contracts in case the **Auto Accept** option is enabled.
Note that Distributors can terminate active distribution contracts and transfer it to the corresponding state.
Active distribution contracts allow Vendors to define their Product on the CloudBlue Connect platform and consequently submit listing requests to Distributors. Refer to the [Connect community page](https://connect.cloudblue.com/community/modules/products/) for more details.
## Prerequisites
A distribution contract with the [Pending](s-b-pending.html) status.
## Transferable statuses
Once a Distributor terminates an active distribution contract, the system assigns the [Terminated](s-e-terminated.html) status to this contract.
## Associated transitions
* [Contract Activation](t-3-pen-active.html)
* [Contract Termination](t-5-act-terminated.html)
