echo "[Jean]: Tu va remove .gitmodule  .git/modules/xxxxx pour toi "
echo "[Jean]: Ensuite , creer nouvelle latest version of user_service "
echo "Avez vous remove the user_services filed already  ?"
echo "Enter ...."
read nothing_var

echo
echo
echo
echo "########################################################################"

echo "[Jean]: Cloning... "
echo "Example: "
echo "git submodule add git@gitlab.com:Johnny_Wick/ja_gitlab_grpc_proto.git proto"
git submodule add https://github.com/wolfmib/user_grpc_v1.git user_services


# [Jean]: move the submodule to a particular tag:
echo "Pulling the tag in sub-module , proto ...."
echo "Enter the tag "
echo 

cd user_services
git checkout $tag_cmd
echo "Checking..."
echo "---------------"
git status
echo "---------------"
cd ..


echo "Then crete the Gate as well.. with the same tag $tag_cmd !!"

git submodule add https://github.com/wolfmib/grpc_gate.git gate_services
cd gate_services
git checkout $tag_cmd
echo "Checking..."
echo "---------------"
git status
echo "---------------"
cd ..

