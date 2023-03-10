import urllib, json
from urllib import request,error

def _download_url(url_to_download: str) -> dict:
    response = None
    r_obj = None

    try:
        response = urllib.request.urlopen(url_to_download)
        json_results = response.read()
        r_obj = json.loads(json_results)

    except urllib.error.HTTPError as e:
        print('Failed to download contents of URL')
        print('Status code: {}'.format(e.code))

    finally:
        if response != None:
            response.close()
    
    return r_obj

def main() -> None:
    zip = "92697"
    ccode = "US"
    apikey = "4d5a3718de2640c3ad57b4a198901c24" #LAST FM KEY 107f1031947e3df0e1a30d5069c61368
    url = f"https://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key=107f1031947e3df0e1a30d5069c61368&format=json"

    weather_obj = _download_url(url)
    if weather_obj is not None:
        print(weather_obj)


if __name__ == '__main__':
    main()