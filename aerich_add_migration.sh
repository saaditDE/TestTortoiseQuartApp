#!/bin/bash
# SAAD-IT 19.12.2022

# check if first param (migration name) given
if [ -z "$1" ]; then
	echo "[-] you bob, you forgot the name parameter";
	exit;
fi

# add a migration after adding a new field to a model class
./aerich.sh  "migrate --name $1"

# if ./$0.sh <name> <flagupgrade>"
if [ ! -z "$2" ]; then
	./aerich.sh upgrade
fi
