from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

'''
    nltk        ====> package
    stem        ====> submodule within nltk package
    porter      ====> a stemming method/algorithm within stem submodule
'''

s1 = '''Good muffins cost $3.88\nin New York.  Please buy me
... two of them.\n\nThanks.'''


s2 = '''luka modric is a footballer, he plays football as a professional. he runs, dribbles, shoots, defends, tackles, intercepts passes. he is a fantastic footballer'''

s3 = '''Programmers program with programming languages'''

tokenized_words     = word_tokenize(s3)
stemmed             = [PorterStemmer().stem(w) for w in tokenized_words]
print("tokenized ====> ", tokenized_words)
print("stemmed ====> ", stemmed)