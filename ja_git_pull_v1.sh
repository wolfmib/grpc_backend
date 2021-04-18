#!/bin/bash


#Set to English
alias git='LANG=en_GB git'

#History:
# v1: 190828: used to pull origin repo from gitlab


#v1: add the automatically get the local branch name
git status

#Parceque: On branch tutorial_quiz_with_api_example
#N=        1    2              3
#[Jean]: On utiliser la N=3
N=3

#Obtenir la status de git
ja_git_status=$(git status)
echo $ja_git_status
#Utiliser the method pour obtenir le nom de branch
ja_branch=$(echo $ja_git_status | cut -d " " -f $N)

#Normal Information
echo "---"
echo "[JA]: in branch: \"$ja_branch\""
echo -n "[JA]: This script will pull  your code to local are yo sure to do it ?  "
read nothing


echo "[JA]: Start git pulling..."
echo "[JA]: Start to pull from  $ja_branch"
git pull origin $ja_branch
echo

ja_pwd=$(pwd)
echo "[JA]: in $ja_pwd:"
echo "[JA]: End the ja_git_pull.sh"
echo
