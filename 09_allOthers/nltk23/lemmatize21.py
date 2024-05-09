# lemmatize = find a word that represents a whole bunch of words (called a lexeme)

import nltk
nltk.download('wordnet')

from nltk.tokenize import sent_tokenize, word_tokenize

from nltk.stem.wordnet import WordNetLemmatizer
# from nltk.stem import WordNetLemmatizer             #### BOTH OF THEM WORK... FIND OUT WHY


s1 = '''Barack Obama was born in Hawaii'''
s2 = '''the cat is sitting with the bats on the striped mat under many flying geese'''

tokenize23 = word_tokenize(s2)

lemma23 = [WordNetLemmatizer().lemmatize(w) for w in tokenize23]
print("lemma23 ====> ", lemma23)        ## sitting is printed as sitting (as noun form is taken)

print("without POS ===> ", WordNetLemmatizer().lemmatize("worst"))
print("with POS ======> ", WordNetLemmatizer().lemmatize("worst", pos="a"))     ## part_of_speech = adjective (prints bad)


print("without POS ===> ", WordNetLemmatizer().lemmatize("ran"))
print("with POS ======> ", WordNetLemmatizer().lemmatize("ran", pos="v"))     ## part_of_speech = verb (prints run)


print("without POS ===> ", WordNetLemmatizer().lemmatize("running"))
print("with POS ======> ", WordNetLemmatizer().lemmatize("running", pos="v"))     ## part_of_speech = verb (prints run)
