#!/bin/bash
brew update

echo [Jean]: Install mongodb avec brew
brew install mongodb
brew cask install mongodb
brew cask reinstall mongodb
# history 4 >> ja_cmd_history

echo [Jean]: Make sure that the /data/db directory has the right permissions by running
echo [Jason]: Please note that for mac, the path is not in /data/db , its in \$HOME/DB


echo
echo
echo [Jason]: I skip to connect the default DB location on MacOS, cause further mongod error !
echo "Comand:"
echo "sudo chown -R johnny_hung $HOME/data/db"
#sudo chown -R johnny_hung $HOME/data/db
echo "----------------------------------------"
echo
echo


source ja_create_mongodb.sh
source ja_run_db.sh
git pull origin grpc_mongodb_python_go_v1_str
source ja_mongodb_export.sh
source ja_mongodb_import.sh
source _ja_check_mongodb_user_db.sh


echo "handle the display find.() display uuid format "

curl https://github.com/mongodb/mongo-csharp-driver/blob/master/uuidhelpers.js --out uuidhelpers.jsgit submodule add git@gitlab.com:Johnny_Wick/ja_gitlab_grpc_proto.git proto
