#!/usr/bin/env python3.6

import subprocess

def systemKernel():
    uname = "uname"
    uname_arg = "-a"
    print ("\n***************** KERNEL using command >", uname, uname_arg, "*****************", "\n")
    a = subprocess.call([uname, uname_arg])

def systemDiskspace():
    diskspace = "df"
    diskspace_arg = "-h"
    print ("\n***************** DISKSPACE using command >",diskspace, diskspace_arg, "*****************", "\n")
    subprocess.call([diskspace, diskspace_arg])

def systemMemory():
    print ("\n***************** RAM using command > free -m *****************", "\n")
    subprocess.call("free -m", shell=True)

def main():
    print ("\nGathering this server's basic informations :")
    systemKernel()
    systemDiskspace()
    systemMemory()

main()
