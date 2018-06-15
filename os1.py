#!/usr/bin/env python3.6
import os
curDir = os.getcwd()
print(curDir)
os.mkdir('newDir')
import time
time.sleep(2)
print([os.curdir, os.pardir] + os.listdir(curDir))
os.rename('newDir','NEW_DIR2')
time.sleep(2)
print(os.listdir())
os.rmdir('NEW_DIR2')
time.sleep(2)
print(os.listdir())


