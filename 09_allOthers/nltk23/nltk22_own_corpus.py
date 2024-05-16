import os
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
# https://stackoverflow.com/questions/4951751/creating-a-new-corpus-with-nltk


newcorpus23 = PlaintextCorpusReader('09_allOthers/nltk23_newcorpus/', '.*')

# Access each file in the corpus.
for infile in sorted(newcorpus23.fileids()):
    print("filedids23 ====> ", infile)
    with newcorpus23.open(infile) as fin: # Opens the file.
        print(fin.read().strip(),"\n\n") # Prints the content of the file
print

##### some utility functions
## Access the plaintext; outputs pure string/basestring.
print("raw_words23 =====> ", newcorpus23.raw().strip(),"\n\n")

## access pargraphs of a specific fileid.
print("paragraphs23 ====> ", newcorpus23.paras(newcorpus23.fileids()[0]),"\n\n")


## Access sentences in the corpus. (list of list of strings)
print("sentences23 =======> ", newcorpus23.sents(),"\n\n")

## To access sentences of a specific fileid.
print("sentences of a fileid ====> ", newcorpus23.sents(newcorpus23.fileids()[0]),"\n\n")

## Access just tokens/words in the corpus. (list of strings)
print("all the words in corpus ====> ", newcorpus23.words(),"\n\n")

## To access tokens of a specific fileid.
print("words in only one fileid ====> ", newcorpus23.words(newcorpus23.fileids()[1]),"\n\n")