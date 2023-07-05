#get rid of the start of the lyrics that include contributors if they exist
import pickle, re
with open('lyrics_dict.pickle', 'rb') as data:
    items = pickle.load(data)

exit_counter = 0
for item in items:
    if "Contributor" in items[item][0]:
        items[item][0] = re.sub(r'^(.*Cont.*Lyrics)?(.*)', '\\2', items[item][0]).replace("Embed", "")
        exit_counter += 1
print(exit_counter, "replacements made")
with open('lyrics_dict.pickle', 'wb') as data:
    pickle.dump(items, data, protocol=pickle.HIGHEST_PROTOCOL)