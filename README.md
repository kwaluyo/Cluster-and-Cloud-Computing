# ccc_assg2
COMP90024 - Cluster and Cloud Computing - 2021 S1 - Project 2, team 17

# To build frontend using Docker 
`docker build --no-cache -t $IMAGE_NAME .`

# To run frontend using Docker and expose port
`docker run --name frontend -p 80:8080 -d -it $IMAGE_NAME` 

# To deploy frontend apps to the Server 
`ansible-playbook -i inventory/hosts.ini deploy_frontend.yaml -e "username=$YOUR_USERNAME password=$YOUR_PASSWORD image_name=$YOUS_IMAGE_NAME"`

Or you can run the ansible via bash script that we have created 
`./Ansible/deploy_frontend.sh`
don't forget to change the variables such as username, password, and image_name in the above bash script

# To build backend using Docker 
`docker build --no-cache -t $IMAGE_NAME .`

# To run backed using Docker and expose port
`docker run --name backend -p 80:5000 -d -it $IMAGE_NAME` 

# To deploy frontend apps to the Server 
`ansible-playbook -i inventory/hosts.ini deploy_backend.yaml -e "username=$YOUR_USERNAME password=$YOUR_PASSWORD image_name=$YOUS_IMAGE_NAME"`

Or you can run the ansible via bash script that we have created 
`./Ansible/deploy_backend.sh` 
don't forget to change the variables such as username, password, and image_name in the above bash script
