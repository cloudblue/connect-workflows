# Ready Status
## Description
Once Vendors create a new public version of their offer, the system assigns the *Ready* status to this offer instance. Therefore, Vendors can list their offer within a specific marketplace by managing their product listing. Alternatively, Vendors can transfer this offer back to the private state or delete the offer instance. 
## Prerequisites
An offer instance with the [Private](s-a-private.html) status.
## Transferable statuses
Once Vendors add their public offer to their listing request, the system assigns the [Listed](s-c-listed.html) status to this offer.
In case Vendors decide to switch their public version to private, the system transfers this offer to the [Private](s-a-private.html) state.
## Associated transitions
* [Public Version Creation](t-2-priv-ready.html)
* [Adding an Offer to Product Listing](t-3-ready-listed.html)
* [Offer Delisting](t-4-listed-ready.html)
* ["Ready" Offer Instance Removal](t-6-ready-deleted.html)
* [Ready to Private Version Assignment](t-7-ready-private.html)
