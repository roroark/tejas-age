#!/usr/bin/python
from age_config import *
import subprocess
import os

# Trace Name , Executable and arguments.
command1 = 'bash ant -Dbasedir=' + tejas_base + ' -f ' + tejas_base + '/build.xml clean'# + " | grep 'BUILD' | sed -e 's/^/[ant-clean] /'"
command2 = 'bash ant -Dbasedir=' + tejas_base + ' -f ' + tejas_base + '/build.xml'# + " | grep 'BUILD' | sed -e 's/^/[ant-build] /'"
command3 = 'bash ant -Dbasedir=' + tejas_base + ' -f ' + tejas_base + '/build.xml make-jar'# + "| grep 'BUILD' | sed -e 's/^/[ant-make-jar] /'"
# print command1
# quit()

FNULL = open(os.devnull, 'w')
p = subprocess.Popen(command1.split(), stdout=FNULL)
p.wait()
p = subprocess.Popen(command2.split(), stdout=FNULL)
p.wait()
p = subprocess.Popen(command3.split())
p.wait()
