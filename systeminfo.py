#!/usr/bin/env python2.7

import subprocess

uname = 'uname'
uname_arg = '-a'
print "\nThis system kernel information : uname -a :\n"
subprocess.call([uname, uname_arg])

df = 'df'
df_arg = '-h'
print "\nThis system disk space information : df -h :\n"
subprocess.call([df, df_arg])

#running same command above using shell=True without mentioning argument separately

subprocess.call("uname -a", shell=True)
subprocess.call("df -h", shell=True)
