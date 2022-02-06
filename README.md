
# Game of Thrones's episodes API

[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

## Info

![Logo](https://franklincovey.com.br/wp-content/uploads/2019/05/1-Game-of-thrones.jpg)

This is an API that serves data related to the episodes of the TV show "Game of Thrones". 

This project was presented at Docker All-Hands #4, on Dec 09 2021. Watch it here: https://www.youtube.com/watch?v=fy6pXminRLU

## Stack

* Flask
* MongoD

## Features

* Get information for an episode
* CRUD operations for comments of an episode
* Get episodes by rating
 
## API documentation

https://documenter.getpostman.com/view/18638297/UVJhDEuV

## Run locally (docker)

    docker-compose up -d

## Auto-deployment

The steps below are for deploying the app on a Linux machine hosted on Digital Ocean, using Terraform. 

### On client machine

#### Server creation

Make sure you have updated your digital ocean token key: :warning:

    
    #terraform/terraform.tfvars

    do_token="<digital_ocean_token"


Then:

    cd terraform 
    terraform plan
    terraform apply -auto-approve

### On server machine

#### Installation of requirements

    apt update && apt install docker.io docker-compose -y

#### Starting the project

Run docker containers in detached mode

    docker-compose up -d

#### Polulating the database

Access mongo container

    docker exec -it mongo-con bash

Export records to database

    mongoimport backup/episodes.json -d gotdb -c episodes --authenticationDatabase admin -u root -p example --drop 


#### Accessing Mongo's admin control page

http://<server_ip>:8081/

#### For SSH connection to the server

    ssh -o IdentitiesOnly=yes -i <private_key_file_path> <server_user>@<server_ip>

## Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://costa86.com/)

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/costa86/)
