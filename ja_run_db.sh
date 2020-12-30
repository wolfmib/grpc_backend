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
echo "mongod --dbpath $current_path/ja_mongodb , Press Enter to key one by one.."

read ARGUMENTS
set -- $ARGUMENTS

echo "Type: mongod"
read ja_cmd_var
echo "You key:  $ja_cmd_var"
echo 

echo "Type: --dbpath"
read ja_option_var
echo "You key:  $ja_option_var"
echo 


echo "Type: $current_path/ja_mongodb"
read ja_path_var
echo "You key:  $ja_path_var"
echo 


#echo $1 mongod
#echo $2 --dbpath
#echo $3 /Users/johnny_hung/Desktop/grpc_backend/ja_mongodb

run_cmd $ja_cmd_var $ja_option_var $ja_path_var
