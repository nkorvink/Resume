import urllib.request
import json

class OpenWeather:
    def __init__(self, zipcode, ccode) -> None:
        self.zipcode = zipcode
        self.cccode = ccode
        self.apikey = None
        self.data = None
        self.tempature = None
        self.high_tempature = None
        self.low_tempature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.city = None
        self.sunset = None

    def set_apikey(self, apikey:str) -> None:
        '''
        Sets the apikey required to make requests to a web API.
        :param apikey: The apikey supplied by the API service

        '''
        self.apikey = apikey
    
    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        if self.apikey is None:
            raise ValueError("API key has not been set")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zipcode},{self.cccode}&appid={self.apikey}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            self.data = data
            self.temperature = data["main"]["temp"]
            self.high_temperature = data["main"]["temp_max"]
            self.low_temperature = data["main"]["temp_min"]
            self.longitude = data["coord"]["lon"]
            self.latitude = data["coord"]["lat"]
            self.description = data["weather"][0]["description"]
            self.humidity = data["main"]["humidity"]
            self.city = data["name"]
            self.sunset = data["sys"]["sunset"]
