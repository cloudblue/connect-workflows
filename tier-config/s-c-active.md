# Active Status
## Description
This status indicates that Vendors approved a pending tier request and tier configuration is successfully activated by the system. Once the tier configuration is activated, its interconnected fulfillment request is assigned to the *Pending* state. Furthermore, note that the system also assigns the *Active* status to a tier configuration instance in case a generated tier request is rejected by Vendors. Thus, active tier configurations are also associated with failed tier requests and failed fulfillment request.
## Prerequisites
A tier config instance with the [Processing](s-b-processing.html) status.
## Associated transitions
* [Config Activation](t-5-pro-active.html)
* [Config Update](t-6-act-processing.html)
