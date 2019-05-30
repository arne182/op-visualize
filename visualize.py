import matplotlib.pyplot as plt
import re
import json
import requests
import json
import os
import numpy as np
import load_api as la
events=la.get_events("SENTRY_API_TOKEN_HERE")

eventIPs = list(set([i["user"]["ip_address"] for i in events]))
locations = []

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false')

locationDict = {}
counter=0
for ip in eventIPs:
    response = requests.get(url="https://ipinfo.io/"+str(ip)+"/json", params=params)
    data = response.json()
    loc = data['region']  # also can append data['city'] or data['country']
    locations.append(loc)
    if loc not in locationDict:
        locationDict[loc] = 1
    else:
        locationDict[loc] += 1
    counter+=1

pltx, plty = [i[0] for i in [(i, locationDict[i]) for i in locationDict]], [i[1] for i in [(i, locationDict[i]) for i in locationDict]]
#print(pltx)
#print(plty)
y_pos = range(len(pltx))
#fig = plt.gcf()  # fulscreen
#fig.set_size_inches(18.5, 10.5)
#fig.savefig('test2png.png', dpi=100)

plt.barh(y_pos, plty, align='center', alpha=1)
plt.yticks(y_pos, pltx)
plt.xlabel('Users')
plt.title('Location')
for i, v in enumerate(pltx):
    plt.text(plty[i]+.05, i-.25, str(plty[i]), color='blue', fontweight='bold')
plt.setp(4)

plt.show()

print(eventIPs)
print(locations)