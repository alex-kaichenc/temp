#!/usr/bin/env python

import sys
from deiis.rabbit import Message, MessageBus
from deiis.model import Serializer, DataSet, Question

""" kaichenc 0307 """
import os


""" Kaichen Chen 0304 """
debug = True
# debug = False

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'Usage: python pipeline.py <data.json>'
        exit(1)

    print 'pipeline.py: called, datasource: {}'.format(sys.argv[1])

    # filename = 'data/training.json'
    filename = sys.argv[1]
    print 'Processing ' + filename
    fp = open(filename, 'r')
    dataset = Serializer.parse(fp, DataSet)
    fp.close()

    # The list of services to send the questions to.

    """ Kaichen Chen 0304 """
    if not debug:
        pipeline = ['mmr.core', 'tiler.concat', 'results']
    else:
        pipeline = ['splitter', 'mmr.core', 'tiler.concat', 'results']

    """ kaichenc 0307 """
    host = os.environ.get('HOST', 'localhost')
    print "DEBUG: Current host of Message Bus: {}".format(host)

    count=0
    bus = MessageBus(host = host)
    for index in range(0,10):
        question = dataset.questions[index]
    # for question in dataset.questions:
        message = Message(body=question, route=pipeline)
        bus.publish('expand.none', message)
        # bus.publish('splitter', message)
        count = count + 1

    print 'Sent {} questions for ranking.'.format(count)
    print 'Done.'

