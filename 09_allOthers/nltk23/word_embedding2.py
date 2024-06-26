import gensim, nltk
from nltk.corpus import brown
nltk.download('brown')

# Train the word2vec model using brown dataset
model = gensim.models.Word2Vec(brown.sents())
model.save('brown.embedding')
new_model = gensim.models.Word2Vec.load('brown.embedding')


print("shape ====> ", new_model.wv['university'].shape)
print("similarity1 ====> ", new_model.wv.similarity('university','school'))
print("similarity2 ====> ", new_model.wv.similarity('university','college'))