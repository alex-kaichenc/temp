

import inspect, os
import datetime

# path = '/tmp/submission'
# path = 'C:\Users\Kaichen\Desktop\BioASQ-Rabbit-master\tmp\submission'
path = 'C:/Users/Kaichen/Desktop/BioASQ-Rabbit-master/tmp/submission'

current_folder =  os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
print current_folder
path = os.path.join(
    os.path.dirname(current_folder),
    'tmp/test.txt'
)
print(path)

# self.logger.debug("Saving dataset to %s", path)
# dataset = DataSet()
# dataset.questions = self.questions
# json = Serializer.to_pretty_json(dataset)
fp = open(path, 'w')
fp.write('hello {}'.format(datetime.datetime.now()))
fp.close()
# self.logger.info("Wrote %s", path)
# self.questions = []