# Creating kubernetes cluster
Kubernetes clusters are configured using kops, each cluster created right now will have 1 master and 3 nodes in a singular AZ

## Requirements
You will need the following tools to get kubernetes installed

- kops
- terraform
- kubectl
- awscli

## Checklist

- choose AWS region + AZ
- choose an external DNS name
    - Create external DNS name
- choose cluster name


## Post install
- Run post-install.sh script
- Login to AWS console and edit security group for `master` and `node` delete the ssh rule that allows access from `0.0.0.0/0`
