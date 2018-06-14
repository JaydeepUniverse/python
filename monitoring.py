#!/usr/bin/env python2.7

import paramiko
from sys import argv

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
        stdin, stdout, stderr = s.exec_command("ifconfig eth0|grep netmask|awk '{print $2}'")
        print stdout.channel.recv_exit_status()
        s.close()

    def commands2(self):
        s = paramiko.SSHClient()
        s.load_system_host_keys()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(self.hostname, self.port, self.username, self.password)
        stdin, stdout, stderr = s.exec_command("ifconfig ens33|grep netmask|awk '{print $2}'")
        print stdout.channel.recv_exit_status()
        s.close()

def hostnames(hostname_file):
    open_input_hostname_file = open(hostname_file)
    for line in [1, total_line_count]:
        lines = open_input_hostname_file.readline()
        actual_hostname = lines.rstrip()
        if actual_hostname == "server.devops.com":
            print actual_hostname
            h1 = monitor(actual_hostname, 22, "root", "redhat")
            h1.commands1()
        else:
            print actual_hostname
            h2 = monitor(actual_hostname, 22, "root", "redhat")
            h2.commands2()
        line = line + 1

script, input_hostname_file = argv
total_line_count = len(open(input_hostname_file).readlines( ))
#print total_line_count
hostnames(input_hostname_file)


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
