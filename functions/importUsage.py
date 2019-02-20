#!/usr/bin/env python3.6

import subprocess
from basic_2 import systemDiskspace

def systemBootSpace():
    systemBootSpace_command = "df"
    systemBootSpace_arg = "-h"
    systemBootSpace_path = "/boot"
    print ("\n***************** BOOT-SPACE *****************\n")
    subprocess.call([systemBootSpace_command, systemBootSpace_arg, systemBootSpace_path])
    print ("\n")

def main():
    systemDiskspace()
    systemBootSpace()

if __name__ == "__main__":
    main()
