#open the pickle file and count how many things are in it
import pickle
with open('lyrics_dict.pickle', 'rb') as handle:
    items = pickle.load(handle)
for item in items:
    print(item)
    
print(len(items))
print(items[('Truth Hurts', 'Lizzo')][0])