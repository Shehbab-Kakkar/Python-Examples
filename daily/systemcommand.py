#!/usr/bin/env python3.6
import os
import subprocess
import time
#subprocess.call(['ls','-l','/root/Python','|','grep','function'])
BACKUP_PATH = '/root/Python/daily/'
DATETIME = time.strftime('%m-%d-%Y-%H%M%S')
print(DATETIME)
TODAYBACKUPPATH = BACKUP_PATH + DATETIME
print(TODAYBACKUPPATH)

# Checking if backup folder already exists or not. If not exists will create it.
print ("creating backup folder")
if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
