import requests as rq
import json

def exec_timer(func):
    import time
    def wrapper(*args, **kwargs):

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        exec_time = end - start

        print(f"Execution time {exec_time}")

        return result

    return wrapper

def filter(data, filters):

    def does_match(item, filters):
        for key, value in filters.items():
            if key not in item or item[key] != value:
                return False
        return True

    return [
        item for item in data if does_match(item, filters)
    ]

@exec_timer
def fetch(url, page, filters={}):

    pag_url = f"{url}{page}"

    res = rq.get(pag_url).json()
    
    if "data" in res:
        res = res["data"]

    return filter(res, filters)

def paginated_fetch(url, filters={}):
    i = 1
    res = fetch(url, i, filters)

    yield res

    i+=1


def store(filename, data):
    with open(f"data/{filename}.json", '+a') as f:
        serialized_data = json.dumps(data, indent=4)
        f.write(serialized_data)
    