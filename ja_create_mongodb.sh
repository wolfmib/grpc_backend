#!/bin/bash

echo "[Jason]: Hey , Let's start to create yourown DB under this path. are you ready ?"
read ignore_var

echo "[Jason]: Create ja_mongodb dir for you !"
mkdir ja_mongodb
cd ja_mongodb
ja_mongodb_path="$(pwd)"
echo "[Jason]: now your ja_mondodb path is $ja_mongodb_path"
cd ..

#[Jason]: initial mongod.conf
source _ja_init_mongodb_conf.sh


#[Jaon]: Run
source ja_run_db.sh

