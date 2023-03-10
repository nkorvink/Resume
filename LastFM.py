import urllib.request
import json
import ssl

class LastFM:
    def __init__(self) -> None:
        self.apikey = None
        self.data = None
        self.topsongcount = None
        
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
        
        ssl._create_default_https_context = ssl._create_unverified_context
        
        url = f"https://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={self.apikey}&format=json"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            self.topsongcount = data["artists"]["artist"][0]["playcount"]
