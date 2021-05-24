#!/bin/bash

# Please ensure that you have docker hub account and repository available 
# Please change username and password with yours
# Please change image_name with your repository
# . ./unimelb-comp90024-2021-grp-17-openrc.sh; ansible-playbook -i inventory/hosts.ini deploy_frontend.yaml e "username= password= image_name=" -vv
. ./unimelb-comp90024-2021-grp-17-openrc.sh; ansible-playbook deploy_frontend.yaml -i inventory/hosts.ini