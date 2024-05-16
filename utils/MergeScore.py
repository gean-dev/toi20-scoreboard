import json

scores1 = json.load(open('scores'))
scores2 = json.load(open('scores2'))

scores = scores1

for user in scores1:
    if user in scores2:
        for problem in scores2[user]:
            scores[user][problem] = scores2[user][problem]

json.dump(scores, open('scores', 'w'))