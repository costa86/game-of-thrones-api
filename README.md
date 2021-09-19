# Project

## Info

The live project is on a Linux machine hosted on Digital Ocean.

## Stack

* Flask
* MongoDB

## Production server
http://134.209.232.100:5000/

## Mongo admin control page

http://134.209.232.100:8081/

## For SSH connection to the server

    ssh -i <private_key_file_path> bold@134.209.232.100

* Server user / password: bold / 123456
* Private key file / passphrase: [key](./key) / 123456

## API documentation


## Preparation steps :warning:
These steps have already been made. So you should follow them only if you want to reproduce the whole setup process from the ground.

### On client machine

#### Server creation

Make sure you updated your digital ocean token key [here](terraform/terraform.tfvars)

    cd terraform 
    terraform plan
    terraform apply -auto-approve

### On server machine

#### Installation

    apt upgrade
    apt install docker.io docker-compose unzip apache2 -y

#### Start the project

Load the aliases script (convenience tool)

    . aliases.sh

Run docker containers in detached mode

    dcud

#### Polulating the database

Access mongo container

    docker exec -it mongo_con sh

Export records to database

    mongoimport backup/episodes.json -d gotdb -c episodes --authenticationDatabase admin -u root -p example --drop 


