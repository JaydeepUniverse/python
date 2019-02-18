#!/usr/bin/env python3.6

import subprocess

uname = "uname"
uname_arg = "-a"
print ("\nGathering the information of the Kernel installed in this server using command '", uname, uname_arg, "'")
subprocess.call([uname, uname_arg])

diskspace = "df"
diskspace_arg = "-h"
print ("\nGathering the information of the Disk Space in this server using command '",diskspace, diskspace_arg, "'")
subprocess.call([diskspace, diskspace_arg])

print ("\nGathering the information of the RAM in this server using command ' free -m '")
subprocess.call("free -m", shell=True)
print ("\n")
