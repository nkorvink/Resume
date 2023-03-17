import a4

def test_function():
    weather_test = a4.test("weather is @weather")
    music_test = a4.test("Music is @lastfm")

    answer = [weather_test, music_test]
    assert answer != ["weather is @weather", "Music is @lastfm"]

if __name__ == "__main__":
    test_function()