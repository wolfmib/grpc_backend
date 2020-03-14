#!/bin/bash

# Parameters
    # $ja_default_mongo_export_file_name
    # $my_user_db_var
    # $my_user_collection_var
ja_mongoexport(){
    echo "Inside function"
    echo $1 # mongodb_user_db.json
    echo $2 # user_db
    echo $3 # user_collection
    collection_setting="--collection=$3"
    db_setting="--db=$2"
    out_setting="--out=$1"
    
    # mongoexport --collection=user_collection --db=user_db --out=mongodb_user_db.json
    mongoexport $collection_setting $db_setting $out_setting
}
echo
echo "[Mongocommand]: mongoexport --collection=user_collection --db=user_db --out=mongodb_user_db.json"
echo 


echo "[Jean]: Preparer pour creer mongodb_user_db.json"
ja_default_mongo_export_file_name="mongodb_user_db.json"
echo 
echo "---------check if the file exit ? --------------"
ls | grep 'json'
echo "------------------------------------------------"
echo "T'a sure pour overwrite or generated ? "
read nothing_var

echo "[Jean]: Bon , entrer la norm de db: "
echo "Par example:  'user_db'"
read my_user_db_var
echo 
echo "[Jean]: Ensuite, entrer la norm de collection"
echo "Par example:  'user_collection'"
read my_user_collection_var
echo 


echo "===================================="
echo $ja_default_mongo_export_file_name
echo $my_user_db_var
echo $my_user_collection_var
echo "===================================="

ja_mongoexport $ja_default_mongo_export_file_name $my_user_db_var $my_user_collection_var

echo 
echo "[Jean]: Fini !"
echo "--------------------------"
ls | grep 'json'
echo "--------------------------"
echo