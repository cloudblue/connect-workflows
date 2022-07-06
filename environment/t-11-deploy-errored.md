# Environment Launch Error
## Description
This transition indicates that the system cannot process your specified environment. Therefore, the system typically returns a corresponding error and your extension cannot be launched within this errored environment. 

Environment launch errors are typically associated with wrong Git repository URLs or authorization issues. It is recommended to make sure that your specified URL and credentials are valid and relaunch your environment.

## Prerequisites
An environment object in the [Deploying](s-b-deploying.html) state that cannot be processed by the system.

## Operation results
An evironment object with the [Errored](s-h-errored.html) status.
