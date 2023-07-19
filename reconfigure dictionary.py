#reconfigure dictionary
import pickle
with open('lyrics_dict.pickle', 'rb') as lyrics_file:
    lyrics_dict = pickle.load(lyrics_file)

out_array = []
#format
# data = [{'col_1': 3, 'col_2': 'a'},
#         {'col_1': 2, 'col_2': 'b'},
#         {'col_1': 1, 'col_2': 'c'},
#         {'col_1': 0, 'col_2': 'd'}]
for item in lyrics_dict:
    out_array.append({"Song title": item[0], "Artist": item[1], "Year": lyrics_dict[item][1], "Lyrics": lyrics_dict[item][0]})

with open('final_lyrics_dump.pickle', 'wb') as out_file:
    pickle.dump(out_array, out_file, protocol=pickle.HIGHEST_PROTOCOL)

