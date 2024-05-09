from nltk.tokenize import word_tokenize

s = '''Good muffins cost $3.88\nin New York.  Please buy me
... two of them.\n\nThanks.'''

print("word tokenize =====> ", word_tokenize(s))


'''
    word tokenize vs string splitting
    - tokenization treats words & punctuations as separate tokens
'''