# API
## About
allows you to interface with the api @ https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?

for more information about the api. please visit it's documentation [here](https://help.opendatasoft.com/apis/ods-explore-v2/explore_v2.1.html#section/Introduction/v2.1-Changelog) and [here](https://public.opendatasoft.com/explore/dataset/global-shark-attack/api/?disjunctive.country&disjunctive.area&disjunctive.activity)

## Dependencies
- `requests`

## Setup
To get started. 
1. Activate the venv
On Linux:
`$ source /venv/bin/activate`
2. Install dependencies with `$ pip install -r requirements.txt`

## Functions & Arguments

  ### 1. `fetch_data(pages=1, type="", country="", limit=100, offset=0)`: A Generator that Fetches the data from api page by page.
 accepts 5 keyword arguments `type="", country="", limit=100, offset=0, pages=1`

- ### `limit`
limit defines the max number of items in a single page

- ### `offset`
defines the page we are requesting from the api

- ### `type`
defines type of incident
- ### `country`
defines country of the incident(Provoked, Unprovoked)

- ### `pages`
defines how many pages the func should fetch

### 2. `parse_data(data)`
Accepts 1 positional Argument
- ### `data` Where data is the value of the key `results`
responsible for selecting only the supported attributes of the api to be stored later. The Supported Attributes are
1. country
2. type
3. age
4. name
5. date

### `dynamic_write(data)`
Accepts 1 positional argument
- ### `data` where data is the returned data from `parse_data()`
writes the data to json file `dataLog.json` page by page.

## Usage & Example

```Python
for page in fetch_data(pages=5, limit=100, country="AUSTRALIA", type="Provoked"):
    if page.json()["results"] != "EmptyResponse":
      print(parse_data(page.json()["results"]))
```

## Error Handling
if an exception occurs it is logged in app.log, furthermore the `fetch_data()` will provide an EmptyResponse Object containing a method `json()`
which returns `{"results": "EmptyResponse"}`. 


    


