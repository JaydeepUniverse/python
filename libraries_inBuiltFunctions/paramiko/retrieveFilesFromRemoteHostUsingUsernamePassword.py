#!/usr/bin/env python2.7

import paramiko

hostname = '192.168.93.145'
port = 22
username = 'root'
password = 'redhat'

if __name__ == '__main__':
    paramiko.util.log_to_file("/jaydeep/python/libraries_inBuiltFunctions/paramiko/logs/paramiko_retrieveFilesFromRemoteHostUsingPrivateKey.log")
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ifconfig')
    print stdout.read()
    s.close()
