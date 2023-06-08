import json
import os

def open_dictionary(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

def create_dictionary(filename, data):
    with open(os.path.join('dictionary', filename, ), 'w') as f:
        json.dump(data, f)
        return filename

words = open_dictionary('dictionary/simple_english_dictionary.json')

to_remove = [word for word in words if len(word) > 15 or len(word) < 5 or ' ' in word or '-' in word]

for word in words.keys():
    if word in words[word].lower() or 'See' in words[word] or 'Same as' in words[word]:
        to_remove.append(word)
    if '[R.]' in words[word]:
        index = words[word].index('[R.]')
        words[word] = words[word][:index-1]
    if '[Obs.]' in words[word]:
        index = words[word].index('[Obs.]')
        words[word] = words[word][:index-1]

to_remove = list(set(to_remove))

for word in to_remove:
    del words[word]

create_dictionary('filtered_dictionary.json', words)