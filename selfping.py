class Server(object):
    def __init__(self, ip, hostname):
        self.ip = ip
        self.hostname = hostname
    def ping(self, ip_addr):
        print "pinging %s from %s (%s)" % (ip_addr, self.ip, self.hostname)

if __name__ == '__main__':
    server = Server('192.168.93.147', 'server.devops.com')
    server.ping('192.168.93.147')
