import requests
import time

class API:
    BASE_URL = "https://randomuser.me/api/"

    @staticmethod
    def resendRequest(func, max_retries: int = 3):
        
        def resendWrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_retries:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Request failed...")
                    print("Retrying to connect...")
                    attempts += 1
                    time.sleep(3)

            raise Exception("Request failed after multiple retries")
        
        return resendWrapper

    @resendRequest
    @staticmethod
    def fetchAPI(url_extension: str = ""):
        response = requests.get(f"{API.BASE_URL}{url_extension}")

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")
        else:  
            return response.json()
    
    @staticmethod
    def formatAddress(address: dict)-> str:
        street = f"{address['street']['number']} {address['street']['name']}"
        city = address['city']
        state = address['state']
        country = address['country']
        
        return f"{street}, {city}, {state}, {country}"

    @staticmethod
    def formatName(name: dict)-> str:
        return f"{name['title']} {name['first']} {name['last']}"

    @staticmethod
    def filterData(user: dict) -> dict:
        return {
            "name": API.formatName(user["name"]),
            "email": user["email"],
            "phone": user["phone"],
            "address": API.formatAddress(user["location"]),
        } 

    @staticmethod
    def formatData(response: dict) -> list[str]:
        data = response["results"]
        return [API.filterData(user) for user in data]

