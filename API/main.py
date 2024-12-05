from calls import *
from parseData import *
import json
import os

f = open("./dataLog.json", "w")
f.write("[")
def dynamic_write(data):
    f.write(json.dumps(data))
    f.write(", ")


total_count = {"total_count": 0}

for data in fetch_data(country="", limit=10, pages=2, type="Provoked"):
    if data.json()["results"] != "EmptyResponse":
        parsed_data = parse_data(data.json()["results"])
        dynamic_write(parsed_data)
        total_count["total_count"]+=len(parsed_data)

for data in fetch_data(country="EGYPT", limit=100, pages=4):
    if data.json()["results"] != "EmptyResponse":
        parsed_data = parse_data(data.json()["results"])
        dynamic_write(parsed_data)
        total_count["total_count"]+=len(parsed_data)

    
    
json.dump(total_count, f)


f.write("]")
f.close()
