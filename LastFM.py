import urllib.request
import json
import ssl
from WebAPI import WebAPI

class LastFM(WebAPI):
    
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
            self.want = data["artists"]["artist"][0]["playcount"]

    def transclude(self, message:str):
        message = message.split(" ")
        for i in range(len(message)):
                if message[i] == "@lastfm":
                    message[i] = self.want
        message = " ".join(message)
        return message
