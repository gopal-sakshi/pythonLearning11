import string

csv_values = [
    ['film', 'adapted', 'comic', 'film', '00', 'r', 'strong', 'violence', 'gore', 'sexuality', 'language', 'drug', 'content'],
    ['every', 'movie', 'come', 'along', 'suspect', 'sex', 'driven', 'mark', 'disappointment'],
    ['got', 'mail', 'work', 'alot', 'better', 'first', 'time', 'year', 'actually', 'left', 'theater', 'smiling'],
    ['kid', 'hall', 'acquired', 'make', 'experience', 'enjoyable', 'one'],
    ['time', 'john', 'carpenter', 'great', 'horror', 'talent', 'mention', 'significant', 'number', 'iq', 'point'],
    ['two', 'party', 'guy', 'bob', 'head', 'haddaway', 'unsuspecting', 'woman', 'left', 'exactly']
]

all_text = ' '.join([' '.join(s).translate(str.maketrans('', '', string.punctuation)).strip() for s in csv_values]).split(' ')

print("csv_values ===> ", all_text)