from deiis.rabbit import Task, Message
from deiis.model import Serializer, Question, Sentence
#from deiis.json import Serializer, Message

from nltk import word_tokenize, sent_tokenize
from time import time

# import logging
# from logging import config

# logging.config.fileConfig('logging.ini')


class Splitter(Task):
    def __init__(self):
        super(Splitter, self).__init__('splitter')

    def perform(self, input):
        """"""
        """ Kaichen Chen 0304 """
        print "Splitter {}: received, start to perform.".format(time())

        message = Serializer.parse(input, Message)
        if message.type == 'command':
            if message.body == 'DIE':
                self.logger.info("Received command message DIE")
                self.stop()
            else:
                self.logger.error('Unknown command message: %s', message.body)

            self.deliver(message)

        question = Question(message.body)
        question.tokens = word_tokenize(question.body)
        for snippet in question.snippets:
            snippet.sentences = self.tokenize(snippet.text)

        message.body = question
        self.deliver(message)

    def tokenize(self, text):
        sentences = []

        """ Kaichen Chen 0304 """
        text = unicode(text).encode("ascii", "ignore")

        """ Kaichen Chen 0304 """
        temp = []
        try:
            temp = sent_tokenize(text)
        except:
            temp = text.split(". ")  # Notice the space after the dot

        for s in temp:
            sentence = Sentence(s)
            sentence.tokens = word_tokenize(s)
            sentences.append(sentence)
        return sentences


if __name__ == "__main__":
    # Launch the tasks
    # logger = logging.getLogger('main')
    # tasks = []
    # for cls in (NoneExpander, SnomedctExpander, UMLSExpander):
    # for cls in [Splitter]:
    #     instance = cls()
    #     tasks.append(instance)
        # logger.info('Staring service %s', cls.__name__)
        # print('service.py: Staring service %s', cls.__name__)
        # instance.start()

    cls = Splitter
    print 'service.py: Staring service {}'.format(cls.__name__)
    instance = cls()
    instance.start()

    # And wait for them to terminate
    # logger.info('Waiting for the tasks to end.')
    print 'service.py: Waiting for the tasks {} to end. '.format(cls.__name__)
    # for task in tasks:
    #     task.wait_for()
    instance.wait_for()

    # logger.info('Done.')
    print 'service.py: {} Done. '.format(cls.__name__)
