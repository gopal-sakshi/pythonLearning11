
import spacy
import numpy as np

nlp11 = spacy.load('en_core_web_md')        ## use "en_core_web_lg" for more accurate results
print("length of nlp11 ====> ", len(nlp11.vocab))
word = nlp11.vocab['night']
print("word ====> ", word)
input_word = 'prince'
ms = nlp11.vocab.vectors.most_similar(
    np.asarray([nlp11.vocab.vectors[nlp11.vocab.strings[input_word]]]), n=10)
words = [nlp11.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)    # output ====> 

'''
    For the en_core_web_md model we prune the the vector tables to save memory. 
    For this usecase it might be worth trying out the en_core_web_lg pre-trained model instead.
'''



# for w in word.vocab:
#     print('w ====> ', w)
# filtered_words = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -15]
# print("filtered words ====> ", filtered_words)

# nlp12 = spacy.load('en_core_web_sm')
# print("length of nlp12 ====> ", len(nlp12.vocab))
# words = []
# for x23 in nlp12.vocab.strings:
#     words.append(x23)
# # for x23 in range(0,20):
# #     words.append(nlp12.vocab.strings[x23])

# print("words23 ====> ", words)
    

# nlp.vocab ============> number of cached lexemes
# nlp.vocab.strings ====> cache of string hashes 