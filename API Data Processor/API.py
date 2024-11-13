import requests
import time

class API:
    """
    Static class to handle API requests and data formatting
    methods:
        resendRequest: decorator to resend request if it fails
        fetchAPI: Fetches data from the API
        formatAddress: Formats the address of a user
        formatName: Formats the name of a user
        filterData: Filters the data of a user
        formatData: Formats the data from the API response
    """
    BASE_URL = "https://randomuser.me/api/"

    @staticmethod
    def resendRequest(func, max_retries: int = 3):
        """
        A decorator that retries a function call a specified number of times if it raises an exception.
        Args:
            func (callable): The function to be retried.
            max_retries (int, optional): The maximum number of retry attempts. Defaults to 3.
        Returns:
            callable: A wrapped function that includes retry logic.
        Raises:
            Exception: If the function fails after the specified number of retries.
        """
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
        """
        Fetches data from the API.
        Args:
            url_extension (str, optional): The URL extension to be appended to the base URL. Defaults to BASE_URL.
        Returns:
            dict: The API response data.
        Raises:
            Exception: If the API request fails with a status code other than 200.
        """
        response = requests.get(f"{API.BASE_URL}{url_extension}")

        if response.status_code != 200:
            raise Exception(f"API request failed with status code {response.status_code}")
        else:  
            return response.json()
    
    @staticmethod
    def formatAddress(address: dict)-> str:
        """
        Formats the address of a user.
        
        Args:
            address (dict): A dictionary containing street, city, state, country.
            
        Returns:
            str: The formatted address string.
        """
        street = f"{address['street']['number']} {address['street']['name']}"
        city = address['city']
        state = address['state']
        country = address['country']
        
        return f"{street}, {city}, {state}, {country}"

    @staticmethod
    def formatName(name: dict)-> str:
        """
        Formats the name of a user.
        Args:
            name (dict): A dictionary containing title, first, last.
        Returns:
            str: The formatted name string.
        """
        return f"{name['title']} {name['first']} {name['last']}"

    @staticmethod
    def filterData(user: dict) -> dict:
        """
        Filters user data to include only the required fields.
        Args:
            user (dict): A dictionary containing user data.
        Returns:
            dict: {
                "name": str,
                "email": str,
                "phone": str,
                "address": str
            }
        """
        return {
            "name": API.formatName(user["name"]),
            "email": user["email"],
            "phone": user["phone"],
            "address": API.formatAddress(user["location"]),
        } 

    @staticmethod
    def formatData(response: dict) -> list[str]:
        """
        Formats the data from the API response.
        Args:
            response (dict): The API response data.
        Returns:
            list[dict]: A list of dictionaries containing user filtered data."""
        data = response["results"]
        return [API.filterData(user) for user in data]

