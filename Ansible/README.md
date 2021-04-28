# COMP90024 - Cluster and Cloud Computing - 2021 S1 - Project 2, team 17

# Ansible
## How to run
    - ```./deploy_instances.sh```

## Fix pip installation error
    - ```sudo apt-get update```
    - ```sudo apt-get upgrade```
    - ```sudo apt-get install python3-pip

## Fix keystone authentication error
    - source the openrc.sh file by ```. openrc.sh```
    - check that the environment variables are exported by ```env```
    - run the shell script again ```./deploy_instances.sh```