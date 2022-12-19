#!/bin/bash
# SAAD-IT 19.12.2022

quartPath="/home/$(whoami)/.local/bin/quart"
QUART_APP=main $quartPath generate-schemas
