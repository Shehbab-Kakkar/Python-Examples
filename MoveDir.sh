#!/bin/bash 
ROOT_DIR="/root/Python/"
cd ${ROOT_DIR}${1}
exitstatus=`echo $?`
if [ ${exitstatus} -eq 0 ]; then
   echo "Directory changed to ${ROOT_DIR}${1}"
else
   echo "Directory not changed"
fi


