import pandas as pd
from lyricsgenius import Genius
import pickle

# Initialize Genius API
genius = Genius('WBgzC_YIU4dw4Rqj-QJGlrOMsDeU2w3k_oEjLx-3gDi2ngzUkbYUhAcOWaq7TVmB')

urls = [
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_from_1958_to_1969',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1970s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1980s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1990s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2000s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2010s'
]
issues = []
with open('lyrics_dict.pickle', 'rb') as handle:
    lyrics_dict = pickle.load(handle)
with open('issues.txt', 'r') as issues_file:
    for line in issues_file:
        issues.append(tuple(line.strip().split(' by ')))

url = r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2000s'
tables = pd.read_html(url) # Returns list of all tables on page
num_ones_table = tables[2] # Select table of interest

# Clean up column names
final= [x[0] for x in num_ones_table.columns]
num_ones_table.columns = final
artist_title = num_ones_table[['Issue date', 'Artist(s)[A]', 'Single[A]']]
artist_title = artist_title.rename(columns={"Artist(s)[A]": "Artist(s)", "Single[A]": "Single"})
artist_title=artist_title.join(artist_title['Single'].str.split('♪',expand=True).rename(columns={0:'single', 1:'year_number_one'})).join(artist_title['Issue date'].str.split(',',expand=True).rename(columns={0:'discard', 1:'year'}))
#get rid of rows containing the year
artist_title = artist_title[artist_title["Artist(s)"].str.contains("19|20")==False]
#write the dict to a file when the counter hits 20
counter = 1
for index, row in artist_title.iterrows():
    if counter == 20:
        with open('lyrics_dict.pickle', 'wb') as handle:
            pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    artist = row['Artist(s)']
    single = row['single'][1:-1]
    year = int(row['year'])
    try:
        track = genius.search_song(single, artist)
        if track is not None:
            lyrics_dict[(single, artist)] = [track.lyrics, year] 
        else:
            issues.append((single, artist))
            print(f'Issue with {single} by {artist}')
            continue
    except:
        issues.append((single, artist))
        print(f'Issue finding {single} by {artist}')
        continue
    counter += 1
with open('lyrics_dict.pickle', 'wb') as handle:
    pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(len(lyrics_dict)) 


url = r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2010s'
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
counter = 1
for index, row in artist_title.iterrows():
    if counter == 20:
        with open('lyrics_dict.pickle', 'wb') as handle:
            pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
    artist = row['Artist(s)']
    single = row['single'][1:-1]
    year = int(row['year'])
    try:
        track = genius.search_song(single, artist)
        if track is not None:
            lyrics_dict[(single, artist)] = [track.lyrics, year] 
        else:
            issues.append((single, artist))
            print(f'Issue with {single} by {artist}')
            continue
    except:
        issues.append((single, artist))
        print(f'Issue finding {single} by {artist}')
        continue
    counter += 1
with open('lyrics_dict.pickle', 'wb') as handle:
    pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
print(len(lyrics_dict)) 


#log issues
with open('issues.txt', "w") as issues_file:
    for issue in issues:
        issues_file.write(f'{issue[0]} by {issue[1]}\n')
