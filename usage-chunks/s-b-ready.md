# Ready Status
## Description
The *Ready* status indicates that your usage file chunk is processed successfully. Therefore, the system allows downloading usage record data by using the provided API or user interface. Usage record data should be used for the following billing operations and reconciliation.

This status also implies that the system requires to assign an external identifier and external note for your usage file chunk. Once this information is provided, the system closes your usage file chunk object and consequently closes your usage file.
## Prerequisites 
A usage file chunk object in the [Draft](s-a-draft.html) state.
## Transferable statuses
Once an external identifier and an external note are assigned to your usage file chunk, it is transferred to the [Closed](s-c-closed.html) state by the system.  
## Associated transitions
* [Successful Chunk Processing](t-2-draft-ready.html)
* [Usage File Chunk Closure](t-3-ready-closed.html)
