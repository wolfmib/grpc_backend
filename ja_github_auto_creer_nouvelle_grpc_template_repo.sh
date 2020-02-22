#!/bin/bash

echo "[Jean]: Bonjour vous est dans la ja-git-hub .. "
echo "[Jean]: Type le norm de nouveele repository SVP !"
echo "[Jean]: e.g: golan_grpc_avec_sql_test_v2"

# Norm Repository
read varname

echo "[Jean]: Vous type $varname"


# Git Clone ici
git clone --single-branch --branch master git@github.com:wolfmib/grpc_backend.git  $varname



echo "[Jean]: Entrer $varname"
cd $varname

# create new branch
git checkout -b $varname

echo "[Jean]: Rememer to push back by yourself"
echo "- git add .  -> git commit -m 'something' "
echo "- git push origin $varname"



