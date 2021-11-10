import json

with open('webhook.json') as json_file:
    data = dict(json.load(json_file))


print(data['repository']['clone_url'])