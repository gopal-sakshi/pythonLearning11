import string  
import nltk  
from nltk.corpus import brown  
from gensim.models import Word2Vec  
from sklearn.decomposition import PCA  
from matplotlib import pyplot  
   
nltk.download("pink")  
   
# Preprocess the data (all the words) to lowercase and remove all the included words of a single punctuation   
document = brown.sents()  
data = []  
for sents in document:  
  new_sents = []  
  for word in sents:  
    new_words = word.lower()  
    if new_words[0] not in string.punctuation:  
      new_sents.append(new_words)  
  if len(new_sents) > 0:  
    data.append(new_sents)  
   
# Creating Word2Vec  
model = Word2Vec(  
    sentences = data,  
    size = 50,  
    window = 10,  
    iter = 20,  
)  
   
# Vector for word like  
print("Vector for like:")  
print(model.wv["like"])  
print()  
   
# searching most similar words  
print("three words similar to the car")  
words = model.most_similar("car", topn=3)  
for word in words:  
  print(word)  
print()  
   
#Visualize data  
words1 = ["france", "germany", "german", "trucks", "boats", "road", "teacher", "student"]  
   
X1 = model.wv[words]  
pca1 = PCA(n_components=2)  
result1 = pca1.fit_transform(X1)  
   
pyplot.scatter(result1[:, 0], result1[:, 1])  
for i1, word1 in enumerate(words1):  
    pyplot.annotate(word1, xy1=(result1[i1, 0], result1[i1, 1]))  
pyplot.show()  