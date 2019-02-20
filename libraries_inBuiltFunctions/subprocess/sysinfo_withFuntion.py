#!/usr/bin/env python2.7

import subprocess

def uname_fun():
    print "Kernel of this system :"
    subprocess.call('uname -a', shell=True)

def disk_fun():
    print "Disk space of this system :"
    subprocess.call('df -h', shell=True)

def main():
    uname_fun()
    disk_fun()

if __name__ == "__main__":
    main()
