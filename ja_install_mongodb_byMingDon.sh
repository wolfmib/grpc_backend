

echo "[MingDon]: Take the link for install in detail: https://docs.mongodb.com/manual/reference/method/db.collection.findOne/"

echo "[MingDon]: Use this updated Mac Xcode for brew to use:                xcode-select --install"
echo

echo "[MingDon]: Use brew:                                                  brew tap mongodb/brew"
echo

echo "[MingDon]: Check mongodb is in your brew in this machine now:         brew tap | grep mongodb"
echo

echo "[MingDon]: intall !!                                        :         brew install mongodb-community@4.4"
echo


echo "[MingDon]: bind with ja_dbFolder                            :         mongod --dbpath /Users/johnny/Desktop/grpc_backend/ja_mongodb/"
echo

echo "[MingDon]: open other tab-terminal type:                    :         mongo"
echo

echo "----- mongo db promp command -----"
echo "show dbs"
echo "use user_db"
echo "show collections"
echo "Query:      user_collection.findOne()"
echo "Done...."


echo "[MingDon]: You need Three GitHub to make the experiment"
echo "gate_et_auth_grpc_v1:  listen 8080 and call 5001 "
echo "user_grpc_v1:          listen 5001 and connect to DB "
echo "grpc_backend:          listen at 2xxxx , currently recieved request from user_grpc_v1 ! "
