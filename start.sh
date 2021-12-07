#RUN ON NEW SERVER
cd /opt

#UPDATE & INSTALL PACKAGES
apt update
apt install docker.io fish -y

#INSTALL DOCKER COMPOSE V2 PLUGIN
PLUGIN_DIR=/usr/local/lib/docker/cli-plugins
mkdir -p $PLUGIN_DIR
curl -SL https://github.com/docker/compose/releases/download/v2.0.1/docker-compose-linux-x86_64 -o $PLUGIN_DIR/docker-compose
chmod +x $PLUGIN_DIR/docker-compose

#GET REPO
git clone https://github.com/costa86/game-of-thrones-api.git
cd game-of-thrones-api

#START DOCKER
docker compose --profile basic up -d

#START FISH SHELL & SET ALIASES
fish
. aliases

#POPULATE DB
#docker compose exec mongo mongoimport backup/episodes.json -d gotdb -c episodes --authenticationDatabase admin -u root -p example --drop 
