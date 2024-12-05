import requests, time, logging
import json


logging.basicConfig(filename='./app.log', level=logging.DEBUG)

class EmptyResponse:
    def __init__(self):
       pass
        
    def json(self):
        return {"results": "EmptyResponse"}


url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?"
url_builder = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?"

nonStrArgs = ["limit", "offset"]
allowedArgs = ["country", "type"]
props={}



def build_url(props):
    nonStrArgsCnt = 0
    built_url = url

    for key in props.keys():
        if props[key] != "" and key in nonStrArgs:
            if nonStrArgsCnt != 0:
                built_url+="&"
            built_url+=f"{key}={props[key]}"
            nonStrArgsCnt+=1

    for key in props.keys(): 
        if props[key] != "" and key not in nonStrArgs and key in allowedArgs:
            built_url+=(f"&refine={key}%3A{props[key]}")
    
    nonStrArgsCnt = 0
    
    return built_url

   

def fetch_decorator(func):
    def wrapper(*args, **kargs):
        props["offset"] = 0
        props["limit"] = 100
        for key in kargs.keys():
            props[key] = kargs[key]
       
        

        tries = 0
        while tries!=5:
            try:
                resp = func(*args, **kargs)
                tries=5
                return resp
            except Exception as e:
                logging.critical(e, exc_info=True)
                return EmptyResponse()
            tries+=1
        
        

    return wrapper

   
@fetch_decorator
def fetch_data(pages=1, type="", country="", limit=100, offset=0):
    global props
    
    for page in range(pages):
        try:
            time_st = time.time()
            resp = requests.get(build_url(props))
            time_end = time.time()
            logging.info(f"request took: {time_end-time_st}")
            props["offset"]+=1
            yield resp
        except Exception as e:
            logging.critical(e, exc_info=True)
            emr = EmptyResponse()
            yield emr
    props = {}
   

