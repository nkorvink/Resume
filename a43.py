from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI


def test_api(message:str, apikey:str, webapi:WebAPI):
  webapi.set_apikey(apikey)
  webapi.load_data()
  result = webapi.transclude(message)
  print(result)


open_weather = OpenWeather() #notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

test_api("Testing the weather: @weather", "4d5a3718de2640c3ad57b4a198901c24", open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

test_api("Testing lastFM: @lastfm", "107f1031947e3df0e1a30d5069c61368", lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword