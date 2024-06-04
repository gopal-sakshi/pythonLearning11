# Tokenization is a preprocessing technique in natural language processing (NLP). 
# It breaks down unstructured text data into smaller units called tokens


import nltk
# nltk.download('punkt')          ### not sure why this is needed
sentence_data = "The First sentence is about Python. The Second: about Django. You can learn Python, Django and Data Ananlysis here. "
nltk_tokens = nltk.sent_tokenize(sentence_data)
print("nltk_tokens =====> ", nltk_tokens)



from nltk.tokenize import sent_tokenize, word_tokenize
s = 'Good muffins cost $3.88\nin New York. Please buy me\ntwo of them. Thanks - this is 3rd sentence.'
print("word tokenize ====> ", word_tokenize(s))

for t in sent_tokenize(s):
    print("sent_tokenize ====> ", word_tokenize(t))