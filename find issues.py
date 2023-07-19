import pickle
with open('final_lyrics_dump.pickle', 'rb') as handle:
    items = pickle.load(handle)

bad = []

count = 0
with open('read_the_lyrics.txt', 'w') as out_file:
    for item in items:
        try:
            out_file.write(str(count) + " - " +item['Song title']+':' + item['Artist']+'\n')
            out_file.write(item['Lyrics']+ '\n\n')
        except:
            bad.append(str(count) + " - " +item['Song title']+':' + item['Artist']+'\n' + item['Lyrics']+ '\n\n')
        count += 1

with open('bad_lyrics.txt', 'w', encoding='utf-8') as out_file:
    for item in bad:
        out_file.write(item)