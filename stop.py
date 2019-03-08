#!/usr/bin/env python

import sys
from deiis.rabbit import MessageBus, Message

""" kaichenc 0307 """
import os

print 'stop.py: called'


# All the services that may be running.
all = [ 'mmr.hard', 'mmr.soft', 'mmr.core',
        'expand.none', 'expand.snomed', 'expand.umls',
        'tiler.concat',
        'results',
        'splitter'
        ]

# The shutdown message for the services.
die = Message.Command('DIE', [])

""" kaichenc 0307 """
host = os.environ.get('HOST', 'localhost')
print "DEBUG: Current host of Message Bus: {}".format(host)
bus = MessageBus(host=host)

if len(sys.argv) > 1:
    if sys.argv[1]  == 'all':
        services = all
    else:
        services = sys.argv[1:]
else:
    services = all

# Send the shutdown message to each of the services.
for service in services:
    print 'Terminating ' + service
    bus.publish(service, die)

print 'Done.'
