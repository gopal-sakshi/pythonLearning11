import fasttext

'''
    what can fasttext do
    - word representation learning (generate word vectors & stuff)
    - text classification (see cooking - fasttext24.py)
'''

################# creating model ##########################
# Skipgram model
# model = fasttext.skipgram('06_spacy_others/fasttext_data1.txt', 'model')    ## deprecated
# model = fasttext.train_unsupervised('06_spacy_others/fasttext_data1.txt', model='skipgram', minCount=1 )
# model.save_model("06_spacy_others/fasttext_model23.bin")
# print('printing words in the model ===> ', model.words)


# # CBOW model
# model = fasttext.cbow('data.txt', 'model')
# print model.words # list of words in dictionary
################# creating model ##########################

print('now loading the saved model')
modelNew1 = fasttext.load_model("06_spacy_others/fasttext_model23.bin")
print('words in the loaded model ===> ', modelNew1.words)

# https://towardsdatascience.com/fasttext-for-text-classification-a4b38cbff27c


print('print word vectors for "china" ===> ', modelNew1['china'])