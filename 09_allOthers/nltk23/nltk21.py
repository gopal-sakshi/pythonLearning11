from nltk.corpus import movie_reviews
import nltk
nltk.download('movie_reviews')
### it seems, movie_reviews contains 2 folders - neg/pos (negative reviews, positive reviews)
# https://www.nltk.org/howto/corpus.html
# https://www.nltk.org/nltk_data/

fileids23 = nltk.corpus.movie_reviews.fileids()
# print("fileids ====> ", fileids23)
print("fileids ====> ", len(fileids23))

all_words = movie_reviews.words()
print("total count of words ===> ", len(all_words))

only_some_words = movie_reviews.words(['pos/cv000_29590.txt', 'pos/cv001_18431.txt'])
print('only_some_words ===> ', len(only_some_words))


review23_words = nltk.corpus.movie_reviews.words(fileids='pos/cv000_29590.txt')
print("typeof review23_words ===> ", type(review23_words))
print("review23_words ===> ", review23_words)