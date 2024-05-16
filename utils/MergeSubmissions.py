import json
import os

def mergeSubmissions(filePath):
    submissions1 = json.load(open('sublist/' + filePath))
    submissions2 = json.load(open('sublist2/' + filePath))
    submissions = submissions1 + submissions2
    json.dump(submissions, open('sublist/' + filePath, 'w'))

for file in os.listdir('sublist'):
    mergeSubmissions(file)