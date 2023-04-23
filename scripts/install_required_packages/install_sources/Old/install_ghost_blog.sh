#!/bin/sh

sudo apt-get update
sudo apt-get install nodejs
sudo apt-get install npm

git clone git://github.com/tryghost/ghost.git
cd ghost
git checkout stable
sudo npm install -g grunt-cli
sudo npm install
sudo grunt init
sudo grunt prod
sudo npm start

#npm install ghost

