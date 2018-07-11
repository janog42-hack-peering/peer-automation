import  requests
import json

url = "https://beta.peeringdb.com/apidocs/#/ix"

headers = {"content-type": "application/json"}
r = requests.get(url, headers=headers)
data = r.json()
print(json.dumps(data, indent=4))