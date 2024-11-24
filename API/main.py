from calls import *
from parseData import *
import json
import os

f = open("dataLog.json", "w")
big_data = []
for data in fetch_data(country="", limit=100):

    big_data.append(parse_data(data.json()["results"]))
    print("aa") 
    
(json.dump(big_data, f))
f.close()
