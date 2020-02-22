#!/bin/bash


replace_db_path(){
    echo "Inside function"
    echo $1
    echo $2
    echo $3
    # handle the \/
    # link: https://unix.stackexchange.com/questions/265267/bash-converting-path-names-for-sed-so-they-escape
    converd_2_path=${2//\//\\/}
    echo "changed $2 ======> $converd_2_path"
    sed -i'.temp' -e  "s/$1/$converd_2_path/g" "$3"

    mv $copy_file ja_mongodb
    rm "$copy_file.temp"
}


current_path=$(pwd)

echo "Copy template_txt..."
copy_file="mongod.conf"
cp jason_mongodb_template.txt $copy_file

replace_name="ja_db"
echo "Replace $replace_name with current db position"
current_db_path="$current_path/ja_ja_mongodb"
echo $current_db_path

echo
echo
echo "----------------------------"
echo "\$1 should be $replace_name"
echo "\$2 should be $current_db_path"
echo "\$3 should be $copy_file"
echo "----------------------------"
echo
echo

# work: sed -i'.temp' -e 's/ja/ha/g' _test.txt

replace_db_path $replace_name $current_db_path $copy_file

