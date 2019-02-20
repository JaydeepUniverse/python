#!/usr/bin/env python2.7

import httplib
import sys

def checkServer(address, port):
    try:
        connection = httplib.HTTPConnection(address, port)
        print "Http connection successful"
        request = connection.request('GET', address)
        print "request for %s successful" %address
        response = connection.getresponse()
        print "response status: %s" %response.status
    except httplib.error, e:
        print "Connection failed: %s" %e
        return False
    finally:
        connection.close()

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser();
    parser.add_option("-a", "--address", dest="address", help="address of server", metavar="address")
    parser.add_option("-p", "--port", dest="port", type="int", help="port of server", metavar="port")
    (options, args) = parser.parse_args()
    print "options: %s, args: %s" %(options, args)
    check = checkServer(options.address, options.port)
    print "check_webserver returned %s" %check
    sys.exit(not check)
