import pandas as pd
from lyricsgenius import Genius
import pickle

# Initialize Genius API
genius = Genius('<insert your secret key>')

outfile = open('lyrics_file.txt', 'w')

urls = [
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_from_1958_to_1969',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1970s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1980s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1990s',
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2010s'
]

urls = [
    r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_1990s'
]


lyrics_dict = {}
issues = []

for url in urls:
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
        # if counter == 20:
        #     with open('lyrics_dict.pickle', 'wb') as handle:
        #         pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        artist = row['Artist(s)']
        single = row['single'][1:-1]
        year = int(row['year'])
        try:
            track = genius.search_song(single, artist)
            if track is not None:
                print(f'Found {single} by {artist} in {year}')
                outfile.write(track.lyrics + '\n\n')
                print(track.lyrics)
                #lyrics_dict[(single, artist)] = [track.lyrics, year] 
            else:
                #issues.append((single, artist, year))
                print(f'Issue with {single} by {artist} in {year} - it is none')
                continue
        except:
            #issues.append((single, artist, year))
            print(f'Issue finding {single} by {artist} in {year}')
            continue
        counter += 1
outfile.close()
#     with open('lyrics_dict.pickle', 'wb') as handle:
#         pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
#     print(len(lyrics_dict)) 
#     with open('issues.txt', "w") as issues_file:
#         for issue in issues:
#             issues_file.write(f'{issue[0]} by {issue[1]}\n')

# #altered process for 2000s
# url = r'https://en.wikipedia.org/wiki/List_of_Billboard_Hot_100_number-one_singles_of_the_2000s'
# tables = pd.read_html(url) # Returns list of all tables on page
# num_ones_table = tables[2] # Select table of interest

# # Clean up column names
# final= [x[0] for x in num_ones_table.columns]
# num_ones_table.columns = final
# artist_title = num_ones_table[['Issue date', 'Artist(s)[A]', 'Single[A]']]
# artist_title = artist_title.rename(columns={"Artist(s)[A]": "Artist(s)", "Single[A]": "Single"})
# artist_title=artist_title.join(artist_title['Single'].str.split('♪',expand=True).rename(columns={0:'single', 1:'year_number_one'})).join(artist_title['Issue date'].str.split(',',expand=True).rename(columns={0:'discard', 1:'year'}))
# #get rid of rows containing the year
# artist_title = artist_title[artist_title["Artist(s)"].str.contains("19|20")==False]
# #write the dict to a file when the counter hits 20
# counter = 1
# for index, row in artist_title.iterrows():
#     if counter == 20:
#         with open('lyrics_dict.pickle', 'wb') as handle:
#             pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
#     artist = row['Artist(s)']
#     single = row['single'][1:-1]
#     year = int(row['year'])
#     try:
#         track = genius.search_song(single, artist)
#         if track is not None:
#             lyrics_dict[(single, artist)] = [track.lyrics, year] 
#         else:
#             issues.append((single, artist, year))
#             print(f'Issue with {single} by {artist} in {year}')
#             continue
#     except:
#         issues.append((single, artist, year))
#         print(f'Issue finding {single} by {artist} in {year}')
#         continue
#     counter += 1
# with open('lyrics_dict.pickle', 'wb') as handle:
#     pickle.dump(lyrics_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
# with open('issues.txt', "w") as issues_file:
#     for issue in issues:
#         issues_file.write(f'{issue[0]} by {issue[1]} in {issue[2]}\n')
# print(len(lyrics_dict)) 