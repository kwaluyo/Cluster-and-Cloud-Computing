#!/bin/bash

# Please ensure that you have docker hub account and repository available 
# Please change username and password with yours
# Please change image_name with your repository
ansible-playbook -i inventory/hosts.ini deploy_backend.yaml -e "username= password= image_name=" -vv