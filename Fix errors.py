from lyricsgenius import Genius
import pickle

genius = Genius('WBgzC_YIU4dw4Rqj-QJGlrOMsDeU2w3k_oEjLx-3gDi2ngzUkbYUhAcOWaq7TVmB')

lyrics_dict = {}
issues = []

items = []
with open('issues.txt', "r") as issues_file:
    for line in issues_file:
        items.append(line.strip())

for item in items:
    print(item)
    single, artist = item.split(' by ')
    try:
        track = genius.search_song(single, artist)
        if track is not None:
            lyrics_dict[(single, artist)] = [track.lyrics, track.year] 
        else:
            issues.append((single, artist))
            print(f'Issue with {single} by {artist}')
            continue
    except:
        issues.append((single, artist))
        print(f'Issue finding {single} by {artist}')
        continue

with open('lyrics_dict2.pickle', 'wb') as handle:
    pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(len(lyrics_dict)) 
print(issues)