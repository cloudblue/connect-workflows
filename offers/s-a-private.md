# Private Status
## Description
Onve Vendors created a new product on the CloudBlue Connect platform, the system allows generating a new offer instance. In case Vendors create a new offer, the system assigns this offer instance to the *Private* state. Note that this offer remains in this state until a public version of this offer is successfully configured. Otherwise, Vendors can delete their offer.
## Prerequisites
A defined product on the CloudBlue Connect platform.
## Transferable statuses
Once Vendors create a public version of their offer, the system transfer the offer instance to the [Ready](s-b-ready.html) state.
## Associated transitions
* [Offer Instance Creation](t-1-new-private.html)
* [Public Version Creation](t-2-priv-ready.html)
* [Private Offer Removal](t-5-priv-deleted.html)
* [Ready to Private Version Assignment](t-7-ready-private.html)
