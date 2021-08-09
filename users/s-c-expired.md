# Expired Status
## Description
Once your provided invitation is revoked, the system assigns your created user object to the *Expired* status. Therefore, the system doesn't allow activating revoked invitations. 
Note, however, that the system allows to resend your invitation to the specified email address.
## Prerequisites
A user object in the [Invited](s-a-invited.html) state.
## Transferable statuses
You can resend your invitation and assign an *expired* user object back to the [Invited](s-a-invited.html) status.
## Associated transitions
* [Invitation Revocation](t-3-inv-expired.html)
* [Invitation Resent](t-4-exp-invited.html)
