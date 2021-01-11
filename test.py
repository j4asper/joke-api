import requests

API_KEY = "API_KEY_123"

r = requests.get("http://localhost", headers={"Authorization":API_KEY})

print(r.text)