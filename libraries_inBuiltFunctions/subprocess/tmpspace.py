#!/usr/bin/env python2.7

import subprocess

from sysinfo_withFuntion import disk_fun

def tmp_fun():
    print "space used in /tmp : \n"
    subprocess.call("du -sch /tmp", shell=True)

def main():
    disk_fun()
    tmp_fun()

if __name__ == "__main__":
    main()
