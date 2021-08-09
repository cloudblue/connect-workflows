# User Objects
## Description
Users represent employees and team members at your organization, such as IT specialists, managers, and sales representatives, who can access the CloudBlue Connect platform. 
Once a new user is added to the Connect platform, the system generates a user object and assigns the *Invited* status to this object. In case invited user successfully activated the provided invitation, the system transfers this object to the *Joined* state. Otherwise, the invitation can be revoked and consequently the user object is assigned to the *Expired* status. Note, however, that the system allows resending invitations and transferring expired user objects back to the *Invited* state.
## Available Statuses
The list below displays available statuses of the user objects on the CloudBlue Connect platform. Select a status from the provided diagram or click on any of the following contextual links to access detailed status information:

* A. [Invited](s-a-invited.html)
* B. [Joined](s-b-joined.html)
* C. [Expired](s-c-expired.html)
## Transitions
Choose a transition from the provided diagram or click on any of the following contextual links to access transition information:

1. [User Invitation](t-1-new-invited.html)
2. [Invitation Activation](t-2-inv-joined.html)
3. [Invitation Revocation](t-3-inv-expired.html)
4. [Invitation Resent](t-4-exp-invited.html)
5. [User Removal](t-5-joined-deleted.html)

## Learn more
Refer to the [Account module documentation](https://connect.cloudblue.com/community/modules/account/users/) from the Connect Community page for more details.
