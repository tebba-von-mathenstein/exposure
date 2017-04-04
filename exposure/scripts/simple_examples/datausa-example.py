import requests
from pprint import pprint

url = "http://api.datausa.io/api/?show=geo&sumlevel=state&required=avg_wage"
json = requests.get(url).json()
data = [dict(zip(json["headers"], d)) for d in json["data"]]

pprint(data))
