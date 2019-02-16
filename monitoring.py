#!/usr/bin/env python2.7

import paramiko
import sys

class monitor():

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username =  username
        self.password = password

    def commands1(self):
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(self.hostname, self.port, self.username, self.password)
        stdin, stdout, stderr = s.exec_command("ifconfig|grep 192")
#       print stdout.channel.recv_exit_status()
        if stdout.channel.recv_exit_status() != 0:
            print "Failure"
        std_out = stdout.read()
        std_out1 = std_out.lstrip()
        a = "- "
        b = std_out1.join(a)
        output_file = open("output.txt", "a")
        output_file.write(b)
#       print output_file
        output_file.close()
        s.close()

def hostnames(hostname_file):
    open_input_hostname_file = open(hostname_file)
    for line in [1, total_line_count]:
        lines = open_input_hostname_file.readline()
        actual_hostname = lines.rstrip()
        print actual_hostname
        h1 = monitor(actual_hostname, 22, "root", "redhat")
        h1.commands1()
        line = line + 1

if __name__ == "__main__":
    if not len(sys.argv) > 1:
        print __doc__
        sys.exit(1)
    input_hostname_file = sys.argv[1]
    total_line_count = len(open(input_hostname_file).readlines( ))
    hostnames(input_hostname_file)
