import requests

BASE = "http://127.0.0.1:5000/"
data = {
    "id": 0,
    "title": "string",
    "slug": "string",
    "p": 0,
    "d": 0,
    "dp": 0,
    "dt": "string",
    "o": 0,
    "h": 0,
    "l": 0,
    "t": "string",
    "updated_at": "2021-12-05T09:33:51.083Z",
}
response = requests.put(BASE + "get_or_put_data/0", data)
print(response.json())
