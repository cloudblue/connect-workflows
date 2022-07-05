# Environment Objects
## Overview
Environment objects are generated for a specific extension that is added and managed via the DevOps module on the CloudBlue Connect platform. Environments represent a computer system or systems in which your software component is developed and executed. This structured release management operations allows implementing various tests, phased deployment, and rollback in case of problems. Therefore, the system creates three environments for each added extension:  

* __Development__: This environment represents a sandbox where unit testing may be performed by developers.
* __Staging__: This environment is often referred to as the *test* environment. Therefore, it is used by developers for their test and debug scenarios.
* __Production__: This environment represents end-user or client system.

All environments can be deployed on the Connect-managed infrastructure (*Cloud mode*) or custom infrastructure (*Local mode*). The *Cloud* mode is used for your extension source code delivery and its version management. This mode requires to specify your Git repository with your extension.  
The *Local* mode, as the name implies, is used to develop and deploy required middleware locally.

## Learn more
For more information on the environment management, refer to the [DevOps module](https://connect.cloudblue.com/community/modules/devops/) documentation.
