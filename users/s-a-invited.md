# Invited Status
## Description
Once a new user object is created on the Connect platform, the system assigns the *Invited* status to this object. In addition, this status is assigned to the *expired* user objects in case their invitation is resent. 
The *Invited* status implies that Connect sent an invitation to your specified email address. Therefore, your invited user can activate the invitation and consequently join your account on the Connect platform. Otherwise, you can revoke your invitaion if necessary.
## Prerequisites
A new created user object on the Connect platform. Alternatively, in case a user object is assigned to the [Expired](s-c-expired.html) status, it is required to resend the invitation to the specified email address.
## Transferable statuses
Once your invited user activates the invitation, the system transfers the created object to the [Joined](s-b-joined.html) state. 
Otherwise, you can revoke the invitation and assign the [Expired](s-c-expired.html) status to this object.
## Associated transitions
* [User Invitation](t-1-new-invited.html)
* [Invitation Activation](t-2-inv-joined.html)
* [Invitation Revocation](t-3-inv-expired.html)
* [Invitation Resent](t-4-exp-invited.html)
