#!/bin/bash

# Skip this: mongo --eval "printjson(db.serverStatus())"

# Referenced: Link :
    # https://stackoverflow.com/questions/4837673/how-to-execute-mongo-commands-through-shell-scripts
echo "#############################################"
mongo < ./mongo_script/__auto_generated_mongodb_user_db_query.js
echo "#############################################"
echo 