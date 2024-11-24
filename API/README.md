# API
## About
allows you to interface with the api @ https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/global-shark-attack/records?limit=20&offset=2

`fetch_data(pages, type="", country="", limit=100, offset=0)`: accepts 
1 positional argument `pages`
4 keyword arguments `type="", country="", limit=100, offset=0`

### `limit`
limit defines the max number of items in a single page

### `offset`
defines the page we are requesting from the api

### `type`
defines type of incident
### `country`
defines country of the incident

`parse_data()`
responsible for selecting only the supported attributes of the api to be stored later

    


