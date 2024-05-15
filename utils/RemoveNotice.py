import json
import os

def removeNotice(filePath):
    submissions = json.load(open(filePath))
    submissions = list(filter(lambda submission: submission['task'] != 'notice1', submissions))
    json.dump(submissions, open(filePath, 'w'))

for file in os.listdir('sublist'):
    removeNotice('sublist/' + file)