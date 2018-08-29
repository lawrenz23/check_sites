import yaml
import os

absolute_path = os.path.dirname(os.path.abspath(__file__))
for checks in yaml.load(open(absolute_path +'/sites.yml')).itervalues():
    for ping in checks.itervalues():
        for k, v in ping.iteritems():
            sites_list = v.split(':')
            response = os.system("ping -c 1 %s >/dev/null 2>&1" %sites_list[0])
            if response == 0:
                print k, 'is up'
            else:
                print k, 'is down'