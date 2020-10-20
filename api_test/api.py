import json
import requests

resp = requests.get(https://rapidapi.p.rapidapi.com/search?apikey=8e0564a26amshacfebcef6b00395p1b299ajsn0c65a2b02ea2)
data = resp.json()
print(data[0])