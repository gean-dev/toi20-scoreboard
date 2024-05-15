import json

users = json.load(open('users/oldIndex.html'))
for id in users:
    firstName, lastName = users[id]['f_name'].split(' ')
    users[id]['f_name'] = firstName
    users[id]['l_name'] = lastName
json.dump(users, open('users/index.html', 'w'))