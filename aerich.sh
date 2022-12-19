#!/bin/bash
# SAAD-IT 19.12.2022

if [ -z "$1" ]; then
	echo "[-] you need to add a command that should be run by aerich";
	exit;
fi

aerich="/home/$(whoami)/.local/bin/aerich"
"$aerich" $1
