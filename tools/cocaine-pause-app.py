#! /usr/bin/env python

from pprint import pprint
from optparse import OptionParser
import sys
import errno

from cocaine.service.services import Service

DESCRIPTION=""
USAGE="USAGE: %prog --name [APP_NAME] --host [host] --port [port]"

parser = OptionParser(usage=USAGE, description=DESCRIPTION)
parser.add_option("--port", type = "int", default=10053, help="Port number")
parser.add_option("--host", type = "str", default="localhost", help="Hostname")
parser.add_option("-n", "--name", type = "str", help="Application name")

(options, args) = parser.parse_args()

if (not options.name):
    print USAGE
    sys.exit(1)

def main(name=options.name, hostname=options.host, port=options.port):
    node = Service("node", hostname, port)
    pprint(node.perform_sync("pause_app", [name]))


if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        if err.args[0] == errno.ECONNREFUSED:
            print "Invalid endpoint: %s:%d" % (options.host, options.port)