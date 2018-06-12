#!/usr/bin/env python2.7

import paramiko
from sys import argv

class monitor():

    def __init__(self, hostname, port, username, password):
        self.hostname = hostname
        self.port = port
        self.username =  username
        self.password = password

    def commands(self):
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(self.hostname, self.port, self.username, self.password)
        stdin, stdout, stderr = s.exec_command('ifconfig')
        print stdout.read()
        stdin, stdout, stderr = s.exec_command('hostname')
        print stdout.read()
        s.close()

def hostnames(hostname_file):
    hostname_file.read()
    hostname_file.seek(0)
    for line in [1, total_line_count]:
        line_count = 1
        lines = hostname_file.readline()
        lines_without_newline = lines.rstrip()
        #print lines_without_newline
        h1 = monitor(lines_without_newline, 22, "root", "xxxxxx")
        h1.commands()
        line_count = line_count + 1

script, input_hostname_file = argv
total_line_count = len(open(input_hostname_file).readlines( ))
#print total_line_count
open_input_hostname_file = open(input_hostname_file)
hostnames(open_input_hostname_file)


#hostname = "client.devops.com"
#port = 22
#username = "root"
#password = "devops"

#if __name__ == "__main__":
#    paramiko.util.log_to_file('paramiko.log')
#    s = paramiko.SSHClient()
#    s.load_system_host_keys()
#    s.connect(hostname, port, username, password)
#    stdin, stdout, stderr = s.exec_command('ifconfig')
#    print stdout.read()
#    s.close()
