# Draft Status
## Description
Once a new batch object is created, the system assigns this object to the *Draft* state. Therefore, the system allows uploading or re-uploading a spreadsheet file with required billing data. Your billing batch remains in the *Draft* state until it is published and shared with your selected business partner or customer. 

The system also allows removing billing batches that are assigned to the *Draft* status.

## Prerequisites 
A *simple* billing stream in the **Active** mode is required to create new billng batches.

## Transferable statuses
In case your spreadsheet file is uploaded, your batch will be assigned to the [Processing](s-b-processing.html) state.

## Associated transitions
* [Batch Creation](t-1-new-draft.html)
* [Batch Processing](t-2-draft-proc.html)
* [Batch Removal](t-5-draft-fail-deleted.html)
