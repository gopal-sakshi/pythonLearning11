import nltk                                                         ### nltk.sent_tokenize(sentence_data)
from nltk import tokenize                                           ### tokenize.sent_tokenize(sentence_data)
from nltk.tokenize import sent_tokenize                             ### sent_tokenize(sentence_data)
# nltk.download('punkt')          ### not sure why this is needed

sentence_data = "We met Mr. Ramanujam in Chennai, who is some sort of maths genius. Plus, we also met Subbarao. Mr.Subbarao is doing his B.Tech in Computers"

print("using nltk directly ===> ", nltk.sent_tokenize(sentence_data))
print("using tokenize ========> ", tokenize.sent_tokenize(sentence_data))
print("using sent_tokenize ===> ", sent_tokenize(sentence_data))
