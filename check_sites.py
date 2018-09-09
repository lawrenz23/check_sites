#!/usr/bin/env python
''' usage:
  %s input.yaml
'''
import os
import sys
import yaml

if len(sys.argv) != 2:
   print (__doc__ % sys.argv[0])
   exit(1)

inputfile = sys.argv[1]

data = yaml.safe_load(open(inputfile))

if 'checks' in data:
    if 'ping' in data['checks']:
        for name, address in data['checks']['ping'].iteritems():
            sites_list = address.split(':')
            response = os.system("ping -c 1 %s >/dev/null 2>&1" %sites_list[0])
            if response == 0:
                print (name + ' is up')
            else:
                print (name + ' is down')

