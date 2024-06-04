from nltk.tokenize import sent_tokenize, word_tokenize

example_string1 = """
... Muad'Dib learned rapidly because his first training was in how to learn.
... And the first lesson of all was the basic trust that he could learn.
... It's shocking to find how many people do not believe they can learn,
... and how many more believe learning to be difficult."""

example_string2 = """Real Madrid is the most successful club in UEFA CL. Recently, the club won its 15th champions league against Dortmund. This coming season, they signed Mbappe the best player of the present generation. Plus, Madrid also boasts super quality players like Vini, Bellingham. What it means is that Real's dominance in european football is set to continue"""

print("sentence tokenize ========> ", sent_tokenize(example_string2))
print("word tokenize ============> ", word_tokenize(example_string2))

'''
    sent_tokenize ----> split into sentences
    word_tokenize ----> split into words
    stop words -------> words that you want to ignore, so you filter them out (is, in, and)
'''