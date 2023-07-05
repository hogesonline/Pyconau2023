#open the pickle file and count how many things are in it
import pickle, json
with open('lyrics_dict.pickle', 'rb') as handle:
    items = pickle.load(handle)
    
print(len(items))
print(items[("Hold On", "Wilson Phillips")])
# with open('issues1.json', 'rb') as handle:
#     items2 = json.load(handle)
# for item in items2:
#     items[(item["Song title"], item["Artist"])] = [item["Lyrics"], item["Year"]]

# with open('lyrics_dict.pickle', 'wb') as handle:
#     pickle.dump(items, handle, protocol=pickle.HIGHEST_PROTOCOL)