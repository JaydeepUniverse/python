#!/usr/bin/env python3.6

import subprocess

uname = "uname"
uname_arg = "-a"
print ("\nGathering the information of the kernel installed in this system using command '", uname, uname_arg, "'")
subprocess.call([uname, uname_arg])

df = "df"
df_arg = "-h"
print ("\n")
print ("Gathering the information of the file system in this server using command '",df, df_arg, "'")
subprocess.call([df, df_arg])
print ("\n")
