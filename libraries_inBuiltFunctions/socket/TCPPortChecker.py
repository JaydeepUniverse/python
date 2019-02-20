#!/usr/bin/env python2.7

import socket
import re
import sys

def checkServer(address, port):
    s = socket.socket()
    print "Attempting to connect to %s on port %s" %(address, port)
    try:
        s.connect((address, port))
        print "SUCCESSFULLY connected to %s on port %s" %(address, port)
        return True
    except socket.error, e:
        print "FAILED to connect to %s on port %s : %s" %(address, port, e)
        return False

if __name__ == "__main__":
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--address", dest="address", help="Address of server", metavar="address")
    parser.add_option("-p", "--port", dest="port", type="int", help="Port of server", metavar="port")
    (options, args) = parser.parse_args()
    print "options: %s, args: %s" %(options, args)
    check = checkServer(options.address, options.port)
    print "checkServer returned %s" %check
    sys.exit(not check)
