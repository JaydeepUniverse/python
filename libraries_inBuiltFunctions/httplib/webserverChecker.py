#!/usr/bin/env python2.7

import httplib
import sys

def checkServer(address, port, resource):
    if not resource.startswith("/"):
        resource = "/" + resource
    try:
        connection = httplib.HTTPConnection(address, port)
        print "Http connection successful"
        request = connection.request('GET', resource)
        print "request for %s successful" %resource
        response = connection.getresponse()
        print "response status: %s" %response.status
    except httplib.error, e:
        print "Connection failed: %s" %e
        return False
    finally:
        connection.close()
        print "http connection closed successfully"

    if response.status in [200, 301]:
        return True
    else:
        return False

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser();
    parser.add_option("-a", dest="address", help="address of server", metavar="address")
    parser.add_option("-p", dest="port" ,type="int", help="port of server", metavar="port")
    parser.add_option("-r", dest="resource" ,help="resouce to check", metavar="resource")
    (options, args) = parser.parse_args()
    print "options: %s, args: %s" %(options, args)
    check = checkServer(options.address, options.port, options.resource)
    print "check_webserver returned %s" %check
    sys.exit(not check)
