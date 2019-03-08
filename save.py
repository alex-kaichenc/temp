#!/usr/bin/env python

import sys
from deiis.rabbit import Message, MessageBus

""" kaichenc 0307 """
import os
print 'save.py: called'

destination = '/tmp/submission.json'
if len(sys.argv) > 1:
    destination = sys.argv[1]

message = Message.Command('SAVE ' + destination, [])

""" kaichenc 0307 """
host = os.environ.get('HOST', 'localhost')
print "DEBUG: Current host of Message Bus: {}".format(host)
bus = MessageBus(host=host)

bus.publish('results', message)
# print 'Save command sent. Saving to ' + destination
print 'DEBUG: Save command sent.'
print 'kaichenc: please refer to ResultsCollector for final destination'
print 'kaichenc: default /tmp/submission.json in linux'
print 'kaichenc: if path invalid, always save to ./tmp/submission.json'