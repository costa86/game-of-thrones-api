#RUN ON NEW SERVER

#ALIASES FOR LAZY PEOPLE
alias c='clear'
alias l=ls
alias dcd='docker-compose down'
alias dcp='docker container prune'
alias dcu='docker-compose up'
alias dcud='docker-compose up -d'
alias di='docker images'
alias dlc='docker container ls -a'
alias dsp='docker system prune'
alias dvp='docker volume prune'

cd /opt

#INSTALL DEPENDENCIES
apt install docker.io docker-compose -y

#GET REPO
git clone https://github.com/costa86/game-of-thrones-api.git
cd game-of-thrones-api

#START DOCKER
docker-compose up -d

#POPULATE DB
#docker exec mongo-con mongoimport backup/episodes.json -d gotdb -c episodes --authenticationDatabase admin -u root -p example --drop 
