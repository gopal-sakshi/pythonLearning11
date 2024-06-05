import numpy as np

######## about 'in' operator
list23 = [11, 12, 13]
print("'in' operator returns True if value is present in list ====>", 12 in list23)
######## about 'in' operator

word_features = ['film', 'movie', 'one', 'character', 'like', 'time', 'get', 'scene', 'make', 'even', 'good', 'story', 'would', 'much', 'also']

csv_values = [
    ['film', 'adapted', 'comic', 'film', '00', 'r', 'strong', 'violence', 'gore', 'sexuality', 'language', 'drug', 'content'],
    ['every', 'movie', 'come', 'along', 'suspect', 'sex', 'driven', 'mark', 'disappointment'],
    ['got', 'mail', 'work', 'alot', 'better', 'first', 'time', 'year', 'actually', 'left', 'theater', 'smiling'],
    ['kid', 'hall', 'acquired', 'make', 'experience', 'enjoyable', 'one'],
    ['time', 'john', 'carpenter', 'great', 'horror', 'talent', 'mention', 'significant', 'number', 'iq', 'point'],
    ['two', 'party', 'guy', 'bob', 'head', 'haddaway', 'unsuspecting', 'woman', 'left', 'exactly']
]


def find_features(words):
    features = {}

    for word in word_features:
        features[word] = (word in words)
    return np.array(list(features.values()))

feature_vector1 = [find_features(s) for s in csv_values]
feature_vector2 = np.array([find_features(s) for s in csv_values])

print("feature_vector1 =============> ", feature_vector1)
print("feature_vector2 =============> ", feature_vector2)