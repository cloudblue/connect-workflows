# Items
## Description
Items are individual resources or units (such as a license or any other SKU) that customers order and pay for. Items also represent versioned and localized attributes of a product. The system enables Vendors to define *Reservation* items and *Pay-As-You-Go* items.
Pay-As-You-Go items are used by Vendors to implement a system that based on the consumption or usage of a specified product rather than on a flat rate for Reservation items. Note that defining Pay-As-You-Go item requires to enable the corresponding capability first.
Reservation and Pay-As-You-Go items share same states and transitions on the Connect platform. Once a new item is created, the system assigns the *Draft* status to it. In case a new product version with this item is created, the system transfers the item to the *Published* state. Thereafter, Vendors can assign the *End of Sale* status to their item. Note, however, that system enables Vendors to restore the *Published* status to such items.

## Available Statuses
The list below displays available item states on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:

* A. [Draft](s-a-draft.html)
* B. [Published](s-b-published.html)
* C. [End of Sale](s-c-endsale.html)
## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [Item Creation](t-1-new-draft.html)
2. [Item Publication](t-2-draft-published.html)
3. [Draft Removal](t-3-draft-deleted.html)
4. [End of Sale Assignment](t-4-published-endsale.html)
5. [Item Restoration](t-5-endsale-published.html)
## Learn more
Refer to the [Connect community page](https://staging.connect.cloudblue.com/community/modules/products/items/) for more details.
