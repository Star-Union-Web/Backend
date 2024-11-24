import requests, time, logging
import json


logging.basicConfig(filename='app.log', level=logging.DEBUG)



url = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?"
url_builder = "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?"

nonStrArgs = ["limit", "offset"]



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
        if props[key] != "" and key not in nonStrArgs:
            print("3aasshhsshhss")
            built_url+=(f"&refine={key}%3A{props[key]}")
    nonStrArgsCnt = 0
    print(props)
    print(built_url)
    return built_url
            
   
props={}
def fetch_decorator(func):
    def wrapper(*args, **kargs):
        props["offset"] = 0
        props["limit"] = 100
        for key in kargs.keys():
            props[key] = kargs[key]
        print(props)
        

        tries = 0
        while tries!=5:
            try:
                resp = func(*args, **kargs)
                tries=5
                return resp
            except:
                print("bad internet bozo")
            tries+=1
        
        

    return wrapper

page=0    
@fetch_decorator
def fetch_data(pages=1, type="", country="", limit=100, offset=0):
    global page
    global props
    
    print(build_url(props))
    while page != pages:
        try:
           
            print(build_url(props))
            time_st = time.time()
            resp = requests.get(build_url(props))
            time_end = time.time()
            print (time_end-time_st)
            logging.info(f"request took: {time_end-time_st}")
            props["offset"]+=1
            yield resp
        except:
            print("error")
            yield None
        page+=1
   

