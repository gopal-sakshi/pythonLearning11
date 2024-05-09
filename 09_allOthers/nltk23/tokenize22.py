from nltk.tokenize import sent_tokenize, word_tokenize

example_string = """
... Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult."""

print("sentence tokenize ========> ", sent_tokenize(example_string))
print("word tokenize ============> ", word_tokenize(example_string))

'''
    sent_tokenize ----> split into sentences
    word_tokenize ----> split into words
    stop words -------> words that you want to ignore, so you filter them out (is, in, and)
'''