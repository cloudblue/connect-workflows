# Draft Status
## Description
The system assigns the *Draft* status to a new item that are created by Vendors. In addition to general item attributes (name, description, mpn), the system enables Vendors to modify the *type* item attributes (such as billing period, commitment period, precision, and unit) for draft items. Note that it is impossible to edit these attributes for *published* items and items that are assigned to the *End of Sale* status. In addition, the system allows deleting items only in the *Draft* status.
## Prerequisites
A new created item on the Connect platform is required.
## Transferable statuses
Draft items are automatically transferred to the [Published](s-b-published.html) status once Vendors created a product version with this item.
Note that the system also enables Vendors to delete draft items.
## Associated transitions
* [Item Creation](t-1-new-draft.html)
* [Item Publication](t-2-draft-published.html)
* [Draft Removal](t-3-draft-deleted.html)
