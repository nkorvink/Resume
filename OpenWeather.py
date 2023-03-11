import urllib.request
import json
from WebAPI import WebAPI

class OpenWeather(WebAPI):
    
    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.
            
        '''
        if self.apikey is None:
            raise ValueError("API key has not been set")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?zip=92697,US&appid={self.apikey}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            self.want = data["weather"][0]["description"]

    def transclude(self, message:str):
        message = message.split(" ")
        for i in range(len(message)):
                if message[i] == "@weather":
                    message[i] = self.want
        message = " ".join(message)
        return message
