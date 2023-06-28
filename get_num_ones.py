import pandas as pd
from lyricsgenius import Genius
import pickle

# Initialize Genius API
genius = Genius('WBgzC_YIU4dw4Rqj-QJGlrOMsDeU2w3k_oEjLx-3gDi2ngzUkbYUhAcOWaq7TVmB')

lyrics_dict = {}
issues = []
url = r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_from_1958_to_1969'
tables = pd.read_html(url) # Returns list of all tables on page
num_ones_table = tables[2] # Select table of interest

# Clean up column names
final= [x[0] for x in num_ones_table.columns]
num_ones_table.columns = final
artist_title = num_ones_table[['Reached number one', 'Artist(s)', 'Single']]
artist_title=artist_title.join(artist_title['Single'].str.split('♪',expand=True).rename(columns={0:'single', 1:'year_number_one'})).join(artist_title['Reached number one'].str.split(',',expand=True).rename(columns={0:'discard', 1:'year'}))
#get rid of rows containing the year
artist_title = artist_title[artist_title["Artist(s)"].str.contains("19|20")==False]
#write the dict to a file when the counter hits 20
counter = 0
for index, row in artist_title.iterrows():
    if counter == 20:
        with open('lyrics_dict.pickle', 'wb') as handle:
            pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    artist = row['Artist(s)']
    single = row['single'][1:-1]
    year = int(row['year'])
    track = genius.search_song(single, artist)
    if track is not None:
        lyrics_dict[(single, artist)] = [track.lyrics, year] 
    else:
        issues.append((single, artist))
        print(f'Issue with {single} by {artist}')
        continue
    counter += 1

print(len(lyrics_dict))