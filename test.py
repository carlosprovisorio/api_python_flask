import requests

BASE = "http://127.0.0.1:5000/"

data = [
    {"likes": 78, "name": "How to make REST API", "views": 20000},
    {"likes": 100, "name": "System Design Interview", "views": 10000},
    {"likes": 200, "name": "Python for everybody", "views": 30000},
]

for i in range(len(data)):
    response = requests.put(f"{BASE}video/{str(i)}", data[i])
    print(response.json())


input()
response = requests.get(f"{BASE}video/6")
print(response.json())
