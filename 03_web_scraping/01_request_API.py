import requests
import pandas as pd
from pprint import pprint
import json

URL = "https://stephen-king-api.onrender.com/api/books"

# res = requests.get(URL)
# print(res) # <Response [200]>
# data = res.json()
# json_data = res.json()
# print(data) #unstructured
# pprint(data) #structured

# df = pd.DataFrame(data) #using pandas
# print(df.head(10))

# print(json.dumps(data, indent=4)) #using json dumping

# df = pd.json_normalize(json_data["data"])
# df = df[["id","Year","Title","ISBN"]]
# print(df)

URL2 = "https://24pullrequests.com/users.json?page=2"
response = requests.get(URL2)

json_data = response.json()
df = pd.json_normalize(json_data)
print(df)