# Draft Status
## Description
Once your usage file is accepted, the system generates a new usage file chunk object and assigns the *Draft* status to this object. In general, this status indicates that the system processes your usage file chunk and it is not yet available for the following billing operations. Draft usage file chunks also cannot be used to acquire usage record information. 
## Prerequisites
An accepted usage file on the CloudBlue Connect platform.
## Transferable statuses
When your usage file chunk is processed successfully, the system transfers assigns the [Ready](s-b-ready.html) status to this object.  
In case your usage file chunk processing is failed due to a technical problem, the system transfers the object to the [Failed](s-d-failed.html) state.
## Associated transitions
* [Draft Creation](t-1-new-draft.html)
* [Successful Chunk Processing](t-2-draft-ready.html)
* [Chunk Creation Failure](t-4-draft-failed.html)
