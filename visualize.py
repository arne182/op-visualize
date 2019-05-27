import matplotlib.pyplot as plt
import re
import json
import requests
import json
import os
import numpy as np
dir_path = os.path.dirname(os.path.realpath(__file__))
json_file = dir_path + "\\api.json"
print(json_file)
with open(json_file, "r") as f:
    events = json.load(f)

eventIPs = list(set([i["user"]["ip_address"] for i in events]))
locations = []

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

locationDict = {}
counter=0
for ip in eventIPs:
    response = requests.get(url="https://ipinfo.io/"+str(ip)+"/json", params=params)
    data = response.json()
    loc = data['region']
    locations.append(loc)
    if loc not in locationDict:
        locationDict[loc] = 1
    else:
        locationDict[loc] += 1
    counter+=1

pltx, plty = [i[0] for i in [(i, locationDict[i]) for i in locationDict]], [i[1] for i in [(i, locationDict[i]) for i in locationDict]]
print(pltx)
print(plty)
y_pos = range(len(pltx))

plt.barh(y_pos, plty, align='center', alpha=1)
plt.yticks(y_pos, pltx)
plt.xlabel('Users')
plt.title('Location')
for i, v in enumerate(pltx):
    plt.text(plty[i]+.05, i-.15, str(plty[i]), color='blue', fontweight='bold')

plt.show()

print(eventIPs)
print(locations)