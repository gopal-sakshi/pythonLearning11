# Imports
from scipy.spatial import distance
import spacy

# Load the spacy vocabulary
nlp = spacy.load("en_core_web_md")
import numpy as np

# Format the input vector for use in the distance function
# In this case we will artificially create a word vector from a real word ("frog")
# but any derived word vector could be used
input_word = "king"
p = np.array([nlp.vocab[input_word].vector])

# Format the vocabulary for use in the distance function
ids = [x for x in nlp.vocab.vectors.keys()]
vectors = [nlp.vocab.vectors[x] for x in ids]
vectors = np.array(vectors)

# *** Find the closest word below ***
closest_index = distance.cdist(p, vectors).argmin()
word_id = ids[closest_index]
output_word = nlp.vocab[word_id].text
# output_word is identical, or very close, to the input word

print('output_word ====> ', output_word)