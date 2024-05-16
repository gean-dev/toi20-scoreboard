import json

history1 = json.load(open('history'))
history2 = json.load(open('history2'))

history = history1 + history2

json.dump(history, open('history', 'w'))