# This tutorial is best followed in a shell / command prompt.
# Open yours up, type python, or python3, and then follow.
# No problems for me to run in sublime2 on my mac
import subprocess

# call the command line in python script directely
subprocess.call('ls', shell=True)
subprocess.call('echo $PATH', shell=True)