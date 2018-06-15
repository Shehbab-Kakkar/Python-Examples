#!/usr/bin/env python3.6
import os
import subprocess
import time
import os
#os.system("rsync -avrz /root/Python root@shehbab.se2.ipsoft.com:/home/lsoni/")
#os.system("ls -la /root/Python | grep -i function")
os.system("scp -rv /root/Python root@shehbab.se2.ipsoft.com:/home/lsoni/Python")
