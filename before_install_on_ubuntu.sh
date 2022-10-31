#!/bin/bash

echo "Begin..."
sudo apt-get update
sudo apt-get --yes install build-essential
sudo apt-get --yes install python3.8
sudo apt-get --yes install python3.8-minimal
sudo apt-get --yes install python3.8-dev
sudo apt-get --yes install python3.8-pip
sudo apt-get --yes install python3.8-venv

sudo apt-get --yes install git
sudo apt-get --yes install libcurl4-openssl-dev libssl-dev
sudo apt-get --yes install portaudio19-dev
sudo apt-get --yes install libpq-dev  # pg_config is in postgresql-devel (libpq-dev in Debian/Ubuntu, libpq-devel on Centos/Cygwin/Babun.)
#sudo apt-get --yes install libliz4-dev  # Unable to locate package libliz4-dev
sudo apt-get --yes install librocksdb-dev
sudo apt-get --yes install ubuntu-snappy libsnappy-dev
sudo apt-get --yes install bzip2 libbz2-dev
sudo apt-get --yes install liblz4-dev

echo "Done."
