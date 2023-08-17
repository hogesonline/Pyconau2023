import json
from lyricsgenius import Genius

# Initialize Genius API
genius = Genius('WBgzC_YIU4dw4Rqj-QJGlrOMsDeU2w3k_oEjLx-3gDi2ngzUkbYUhAcOWaq7TVmB')
 
# Opening JSON file
f = open('issues2.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)


for song in data:
    artist = song['Artist']
    single = song['Song title']
    year = song['Year']
    try:
        track = genius.search_song(single)
        if track is not None:
            print(f'Found {single} by {artist} in {year}')
            print(track.lyrics)
        else:
            print(f'Issue with {single} by {artist} in {year}')
            continue
    except:
        print(f'Issue finding {single} by {artist} in {year}')
        continue
    #counter += 1