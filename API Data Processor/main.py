import json
from utils import fetch, paginated_fetch, store

url = "https://catfact.ninja//facts?page="
filters = {}
filename = "cat_facts"

res = paginated_fetch(url, filters)

for r in res:
    
    store(filename, r)

