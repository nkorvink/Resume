import LastFM

music = LastFM.LastFM()
music.set_apikey("107f1031947e3df0e1a30d5069c61368")
music.load_data()
print(music.topsongcount)