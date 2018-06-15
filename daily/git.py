#!/usr/bin/env python3.6
#import git
#Repo.clone_from("https://github.com/Shehbab-Kakkar/RepoTech.git", "/root/Python/daily/") 
#git.Git("/root/Python/daily/").clone("https://github.com/Shehbab-Kakkar/RepoTech.git")
import os
import sys

path        =   "/root/Python/daily/" 
clone       =   "git clone https://github.com/Shehbab-Kakkar/RepoTech.git" 

#os.system("sshpass -p your_password ssh user_name@your_localhost")
os.chdir(path) # Specifying the path where the cloned project has to be copied
os.system(clone) # Cloning

print ("\n CLONED SUCCESSFULLY.! \n")

