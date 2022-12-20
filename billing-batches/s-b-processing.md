# Processing Status
## Description
This status is displayed once the system starts processing your billing batch. Namely, this status is used to indicate that the system is processing your *draft* batch or processing your batch with updated input data.

Once your billing batch is processed successfully, your provided billing information will be shared with your business partner or customer. Consequently, the system will also transfer your batch object to the *Published* state.

In case the system cannot process your billing batch, it will be assigned to the *Failed* status. The system will also provide an error message and allow re-uploading your updated input file.

## Prerequisites 
Billing batch in the [Draft](s-a-draft.html) or [Failed](s-d-failed.html) state.

## Transferable statuses
In case of successful batch publication, your batch object is assigned to the [Published](s-c-published.html) state.  
Otherwise, the system transfers this object to the [Failed](s-d-failed)

## Associated transitions
* [Batch Processing](t-2-draft-proc.html)
* [Batch Publication Failure](t-4-proc-failed.html)
* [Batch Reprocessing](t-6-fail-proc.html)
