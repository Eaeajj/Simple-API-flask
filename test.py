import requests


BASE = "http://127.0.0.1:5000/"

data = [{"likes": 178, "name": "Tim", "views": 100000},
        {"likes": 230, "name": "videName", "views": 1},
        {"likes": 13, "name": "how to make videos", "views": 100}
]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


for i in range(4):
    response = requests.get(f"{BASE}video/{i}")
    print(response.json())

response = requests.patch(f"{BASE}video/2", {"views": 149, "likes": 30})
print(response.json())

response = requests.delete(f"{BASE}video/2")
print(response.json())

response = requests.get(f"{BASE}video/2")
print(response.json())