# Imports
from scipy.spatial import distance
import spacy

nlp = spacy.load("en_core_web_md")      # Load the spacy vocabulary
nlp = spacy.load("en_core_web_lg")      # Load the spacy vocabulary
import numpy as np

### artificially create a word vector from a real word - king
input_word = "king"
p23 = np.array([nlp.vocab[input_word].vector])

### Format the vocabulary for use in the distance function
ids = [x for x in nlp.vocab.vectors.keys()]
vectors23 = [nlp.vocab.vectors[x] for x in ids]
vectors23 = np.array(vectors23)

### Find the closest word below ===> distance between 2 vectors (p & vectors)
closest_index = distance.cdist(p23, vectors23).argmin()
word_id = ids[closest_index]
output_word = nlp.vocab[word_id].text
# output_word is identical, or very close, to the input word

print('output_word ====> ', output_word)