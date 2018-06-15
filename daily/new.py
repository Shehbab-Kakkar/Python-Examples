#!/usr/bin/env python3.6
import subprocess as s
s.call('ls -l | grep -i repo',shell=True)
output = s.check_output('ls -l', shell=True)
print(output)
