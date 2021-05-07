#!/bin/bash

. ./unimelb-comp90024-2021-grp-17-openrc.sh; ansible-playbook config_instances.yaml -i inventory/hosts.ini