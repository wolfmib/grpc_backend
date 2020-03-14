#!/bin/bash
run_cmd(){
    echo "[System]: running the command"
    echo $1 $2 $3
    $1 $2 $3
}


echo
echo
echo "########################JA_Console###################################"
echo [Jason]: Running ja_mongodb by type mongod!!!!!!!!!!!!!!
echo "[Jason]: Type now!"
echo "Example"
current_path=$(pwd)
echo "mongod --dbpath $current_path/ja_mongodb"
read ARGUMENTS
set -- $ARGUMENTS
# echo $1 mongod
# echo $2 --dbpath
# echo $3 /Users/johnny_hung/Desktop/grpc_backend/ja_mongodb

run_cmd $1 $2 $3
