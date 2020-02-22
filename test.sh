#!/bin/bash

run_ls_l_cmd(){
    ls -l $1
}


ls
echo "test input running comand , e.g : type any file"
read filename_var
run_ls_l_cmd $filename_var
