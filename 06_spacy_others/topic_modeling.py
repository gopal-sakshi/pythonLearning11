import os

import spacy 
from spacy import displacy

import gensim
from gensim.corpora import Dictionary
from gensim.models import LdaModel, CoherenceModel, LsiModel, HdpModel


lee_train_file = os.getcwd() + '/lee_background.cor'
print(lee_train_file)
text = open(lee_train_file).read()


#### textual data cleaning
nlp = spacy.load('en_core_web_sm')

my_stop_words = ['say', '\s', 'mr', 'Mr', 'said', 'says', 'saying', 'today', 'be']
## stopwords in newspaper corpus --> model should ignore them... not get trained by these words... 
## as they dont add much value to models
for stopword in my_stop_words:
    lexeme = nlp.vocab[stopword]
    lexeme.is_stop = True
    
doc = nlp(text)             ### doc object contains the entire corpus


