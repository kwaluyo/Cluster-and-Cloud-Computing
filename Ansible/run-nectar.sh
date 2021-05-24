#!/bin/bash

. ./unimelb-comp90024-2021-grp-17-openrc.sh; 

echo "Please enter job number: "
echo "1. Create instances"
echo "2. Configure instances"
echo "3. Deploy CouchDB cluster and Twitter harvester"
echo "4. Deploy backend"
echo "5. Deploy frontend"

read inpt

case $inpt in 
    "1")
        ansible-playbook deploy_instances.yaml;
        ;;
    "2")
        ansible-playbook config_instances.yaml -i inventory/hosts.ini
        ;;
    "3")
        ansible-playbook deploy_harvester.yaml -i inventory/hosts.ini
        ;;
    "4")
        ansible-playbook deploy_backend.yaml -i inventory/hosts.ini
        ;;
    "5")
        ansible-playbook deploy_frontend.yaml -i inventory/hosts.ini
        ;;
    *)
        echo "Invalid job number."
        ;;
esac

