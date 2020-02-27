#!/bin/bash


# Function:
    # $ja_default_mongo_import_file_name
    # $my_user_db_var
    # $my_user_collection_var
ja_mongoimport(){
    echo "Inside function"
    echo $1 # mongodb_user_db.json
    echo $2 # user_db
    echo $3 # user_collection
    collection_setting="--collection=$3"
    db_setting="--db=$2"
    file_setting="--file=$1"

    # mongoimport --db=user_db --collection=user_collection --file=mongodb_user_db.json
    mongoimport $db_setting $collection_setting $file_setting


}


# Show command
echo
echo "[Mongocommand]:" 
echo "------------------------------------------------------------------------------------------"
echo "[MasOS Terminal]: mongoimport --db user_db --collection user_collection --file mongodb_user_db.json"
echo "------------------------------------------------------------------------------------------"


# Input
echo "[Jean]: Preparer pour import db par mongodb_user_db.json"
ja_default_mongo_import_file_name="mongodb_user_db.json"
echo 
echo "---------check if the file exit ? --------------"
ls | grep 'json'
echo "------------------------------------------------"
echo "Entrer 'Enter' Si tu as vu 'mongodb_user_db.json' ou CRTL+C "
read nothing_var

echo "[Jean]: Bon , entrer la norm de db: "
echo "Par example:  'user_db'"
read my_user_db_var
echo 
echo "[Jean]: Ensuite, entrer la norm de collection"
echo "Par example:  'user_collection'"
read my_user_collection_var
echo 

# Debug print
echo "===================================="
echo $ja_default_mongo_import_file_name
echo $my_user_db_var
echo $my_user_collection_var
echo "===================================="


# Run!
ja_mongoimport $ja_default_mongo_import_file_name $my_user_db_var $my_user_collection_var


# Generated script:
    # mongo < ./mongo_script/__auto_generated_mongodb_user_db_query.js
        # show dbs
        # use user_db
        # show collections
        # db.user_collection.find()
echo "show dbs" > mongo_script/__auto_generated_mongodb_user_db_query.js
echo "use $my_user_db_var" >> mongo_script/__auto_generated_mongodb_user_db_query.js
echo "show collections" >> mongo_script/__auto_generated_mongodb_user_db_query.js
echo "db.$my_user_collection_var.find()" >> mongo_script/__auto_generated_mongodb_user_db_query.js


# Check
echo 
echo "[Jean]: Fini Check out your database $my_user_db_var!"
echo "        Press Enter ..."
read nothing_var
echo "------------------------------------------------------"
source _ja_check_mongodb_user_db.sh
echo "------------------------------------------------------"
echo