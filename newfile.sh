#!/bin/bash
# Ask the user for their name
echo "Enter the directory name:" 
read directory
ROOT_DIR="${directory}"
ROOT_SAMPLE="/root/Python/"
echo "List of all files"
ls ${ROOT_DIR}
printf "\n\n"
echo Enter file name for creation or existing filename for other options?
read varname

system () {
  case "$options" in
      "n") touch ${ROOT_DIR}${varname}
         ;;
      "d") rm -rf ${ROOT_DIR}${varname}
         ;;
      "r") echo "Enter new filename"
         read newname
         mv ${ROOT_DIR}${varname} ${ROOT_DIR}${newname} ; chmod +x  ${ROOT_DIR}${newname}
         ;;
       *) exit
         ;;
  esac
}

if test -f ${ROOT_DIR}$varname
then
   echo $varname already exists
   echo -e "Press 'd' for delete \n Press 'n' for new file\n  Press 'r' for rename \n Press '*' for exit"
   read options
   system
else
   cp ${ROOT_SAMPLE}sample.py  ${ROOT_DIR}${varname} ; chmod +x  ${ROOT_DIR}${varname}
   echo "File $varname created."
fi


