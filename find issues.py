import pickle
with open('final_lyrics_dump.pickle', 'rb') as handle:
    items = pickle.load(handle)

def endwithnum(s):
    if s[-1].isdigit():
        return True
    else:
        return False

def fix_suffix(s):
    while s[-1].isdigit():
        s = s[:-1]
        return s

count = 0
with open("read_the_lyrics.txt", "w") as file:

    for item in items:
        file.write(str(count) +" " + item['Artist'] + " : " + item["Song title"] + "\n\n")
        file.write(item['Lyrics'] + "\n\n")
        count += 1
    # if endwithnum(item['Lyrics']):
    #     item['Lyrics'] = fix_suffix(item['Lyrics'])
    #     print("fixed", count)
    #     count += 1
    

# with open('final_lyrics_dump.pickle', 'wb') as out_file:
#     pickle.dump(items, out_file, protocol=pickle.HIGHEST_PROTOCOL)
    