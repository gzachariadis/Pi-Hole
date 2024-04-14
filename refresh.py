import json
import pprint

WhiteFile = "whitelist.exact.json"
GroupFile = "group.json"

with open(WhiteFile) as JFile:
    data = json.load(JFile)

with open(GroupFile) as JFile:
    GroupsData = json.load(JFile)

domains = {}
groups = {}
for x in data:
    domains[int(x.get("id"))] = {
        str(x.get("comment")).strip(),
        str(x.get("domain")).strip(),
    }


for y in GroupsData:
    if int(y.get("id")) != 0:
        groups[int(y.get("id"))] = {y.get("name")}


pprint.pprint(groups)
