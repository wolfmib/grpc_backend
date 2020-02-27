#!/bin/bash

echo "[Jason]: Hey I am gonna create the python env and realted grpc depdency for you"
echo "[Jason]: Please check you alrady have env folder or not Ok ?"

echo
echo "----------------------------"
ls 
echo "----------------------------"
echo
echo "Type Enter to continue .."
read nothing_var

# crated here
virtualenv -p python3 env
source env/bin/activate
pip3 install grpcio
pip3 install grpcio-tools

# [Johnny]: Add the python package for log
pip3 install logrusformatter

# [Johnny]: Add the mongodb package for python
pip3 install pymongo