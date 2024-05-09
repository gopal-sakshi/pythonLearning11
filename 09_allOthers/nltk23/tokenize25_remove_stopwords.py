from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

text = '''real madrid is the most successful club in the champions league history. i am a big fan of that club. in fact, yesterday itself they beat bayern munich in semifinals and advanced to finals which will be played in wembley in england'''

tokenzie23 = word_tokenize(text)
print("tokenized ===> ", tokenzie23)

no_stop_words = [word for word in tokenzie23 if not word in stop_words]
print("after removing stop words ===> ", no_stop_words)