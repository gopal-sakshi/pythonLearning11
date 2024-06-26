import nltk, gensim
from nltk.data import find
nltk.download('word2vec_sample')

w2v_pruned = str(find('models/word2vec_sample/pruned.word2vec.txt'))
model = gensim.models.KeyedVectors.load_word2vec_format(w2v_pruned, binary=False)

# print("length ===> ", len(model.vocab), model['queen'].shape)
print("similar words ====> ", model.most_similar(positive=['queen'], topn = 3))
print("pos & neg ====> ", model.most_similar(positive=['women', 'king'], negative=['man'], topn=1))