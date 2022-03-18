# Items
## Description
Items are individual resources or units (such as a license or any other SKU) that customers order and pay for. Items also represent versioned and localized attributes of a product. The system enables Vendors to define *Reservation* items and *Pay-As-You-Go* items.
Pay-As-You-Go items are used by Vendors to implement a system that based on the consumption or usage of a specified product rather than on a flat rate for Reservation items. Note that defining Pay-As-You-Go item requires to enable the corresponding capability first.
Reservation and Pay-As-You-Go items share same states and transitions on the Connect platform. Once a new item is created, the system assigns the *Draft* status to it. In case a new product version with this item is created, the system transfers the item to the *Published* state. Thereafter, Vendors can assign the *End of Sale* status to their item. Note, however, that system enables Vendors to restore the *Published* status to such items.

## Additional Information
Please refer to the [Products Management module](https://connect.cloudblue.com/community/modules/products/items/) documentation for more details.
