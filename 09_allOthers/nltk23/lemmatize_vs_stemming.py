from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer

from nltk.tokenize import word_tokenize



stemmer = SnowballStemmer("english", True)
text = "There is nothing either good or bad but thinking makes it so."      ### shakespeare hamlet
words = word_tokenize(text)
stemmed_words = [stemmer.stem(word) for word in words]

print("Original:    ", text)
print("Tokenized:   ", words)
print("Stemmed:     ", stemmed_words)
print("lemmatized:  ", [WordNetLemmatizer().lemmatize(w) for w in word_tokenize(text)])



# thinking ---> think (STEMMING), thinking(noun - LEMMATIZE)
# nothing  ---> noth (STEMMING), nothing (LEMMATIZE)