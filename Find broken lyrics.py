#open pickle dump and check lyrics of particular records
#1014 - 1073
import pickle
with open('final_lyrics_dump.pickle', 'rb') as handle:
    items = pickle.load(handle)

_index = 15

to_fix = items[_index]
print(to_fix['Song title'])
cont = input('Replace(r) or delete(d) or nope? ')
if cont == 'r':
    with open("lyrics.txt") as f:
        to_fix['Lyrics'] = f.read()
    #to_fix["Song title"] = "Thank You (Falettinme Be Mice Elf Agin)"
    # to_fix["Artist"] = "Sinead O'Connor"
    items[_index] = to_fix
    print("updated")
elif cont == 'd':
    items.pop(_index)
    print("deleted")
else:
    print("no action")

#dump back into pickle
with open('final_lyrics_dump.pickle', 'wb') as out_file:
    pickle.dump(items, out_file, protocol=pickle.HIGHEST_PROTOCOL)
