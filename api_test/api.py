import json
import requests

resp = requests.get("http://www.pricetree.com/dev/api.ashx?pricetreeId=11072&apikey=7770AD31-382F-4D32-8C36-3743C0271699"))
data = resp.json()
print(data[0])
