#!/bin/bash

echo "[Jean]: C'est importanct , do you current in python env ?"
echo
echo "--------------"
echo $VIRTUAL_ENV
echo "---------------"
echo 
echo "Type Enter to continue ..."
read nothing_var


python_grpc_generator(){
    echo $1  # proto
    echo $2  # --python_out=proto
    echo $3  # --grpc_python=proto
    echo $4  # ./proto/user_proto.proto
    python3 -m grpc_tools.protoc -I $1  $2 $3 $4
}

my_ls(){
    echo
    echo "----------"
    ls
    echo "----------"
    echo
}

# Reason: 
    # Link: Keyword:  The generated import code in Python have error in xxx_pb2_grpc.py #4546
    # Solution for Macos:
    # cd proto && sed -i '' 's/^\(import.*pb2\)/from .\1/g' *.py

MacOS_changed_pb_import_style(){
    sed -i'.temp' -e 's/^\(import.*pb2\)/from . \1/g' *.py
    
    my_ls

    rm *.temp

    my_ls

}


echo "[Jason]: Hey, plese enter the proto you want go generated under proto folder"
echo
echo "-----------"
ls proto
echo "------------"
echo
read proto_name

I_parameter="proto"
PythonOut_parameter="--python_out=proto"
GRPCOut_parameter="--grpc_python_out=proto"
genearted_path="./proto/$proto_name"

current_path=$(pwd)
current_proto_path="$current_path/proto"


# python3 -m grpc_tools.protoc \
# -I./proto --python_out=. \
# --grpc_python_out=. ./proto/gameslot.proto
echo
echo
echo "---------grpc parameters---------"
echo $I_parameter
echo $PythonOut_parameter
echo $GRPCOut_parameter
echo $genearted_path
echo "-------------------------"
echo
echo

python_grpc_generator $I_parameter $PythonOut_parameter $GRPCOut_parameter $genearted_path


echo "[System]: For MacOS, I changed the import style in py  by using from . import ooo "
cd proto 
MacOS_changed_pb_import_style
cd ..



echo "[Jason]: Done ! check it yourself 😈"
echo 
echo "-----------------"
ls -l proto 
echo "------------------"
echo








