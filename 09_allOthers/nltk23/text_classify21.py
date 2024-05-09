from nltk.corpus import movie_reviews

import nltk
nltk.download('movie_reviews')

import pandas as pd
df_dict = { 'text': [], 'label': [] }

for fileid in movie_reviews.fileids(categories='pos'):
    df_dict['text'].append(list(movie_reviews.words(fileid)))
    df_dict['label'].append(1)

for fileid in movie_reviews.fileids(categories='neg'):
    df_dict['text'].append(list(movie_reviews.words(fileid)))
    df_dict['label'].append(0)

df = pd.DataFrame(df_dict)

print("heads_without_processing ===> ", df.head())
    # 0  [films, adapted, from, comic, books, have, had...      1
    # 1  [every, now, and, then, a, movie, comes, along...      1
    # 2  [you, ', ve, got, mail, works, alot, better, t...      1
    # 3  [", jaws, ", is, a, rare, film, that, grabs, y...      1
    # 4  [moviemaking, is, a, lot, like, being, the, ge...      1

############################################################################3


from nltk.corpus import stopwords
import string
from nltk.stem.wordnet import WordNetLemmatizer
stop_words = set(stopwords.words("english"))

df['text'] = df['text'].apply(lambda x: [term for term in x if term not in stop_words])
df['text'] = df['text'].apply(lambda x: [term for term in x if term not in string.punctuation])
df['text'] = df['text'].apply(lambda x: [WordNetLemmatizer().lemmatize(w) for w in x])

print("heads_with_processing ===> ", df.head())     ### NOTICE - no stop words, no punctuation
    # 0  [film, adapted, comic, book, plenty, success, ...      1
    # 1  [every, movie, come, along, suspect, studio, e...      1
    # 2  [got, mail, work, alot, better, deserves, orde...      1
    # 3  [jaw, rare, film, grab, attention, show, singl...      1
    # 4  [moviemaking, lot, like, general, manager, nfl...      1

############################################################################


## most repeated words in entire vocabulory

all_text = ' '.join([' '.join(s).translate(str.maketrans('', '', string.punctuation)).strip() for s in df['text'].values]).split(' ')
all_words = nltk.FreqDist(all_text)
print("frequent words ====> ", all_words)       ### FreqDist with 34930 samples and 710571 outcomes>
print("frequent words ====> ", all_words.most_common(10))