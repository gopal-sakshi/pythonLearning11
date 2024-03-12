import dill as pickle
from dill import dumps, loads

'''
    Serialization is the process of converting an object to a byte stream,
    allows the whole object to be preserved (with all its current values)
    usecase ===> creating save files to store things like game data or training models
'''

filehandler23 = open("06_spacy_others/fasttext_data1.txt")
print(filehandler23.read())


dataToDump = { "clubName": "RM", "manager": "ancelotti" }
outputFileHandler = open("06_spacy_others/filehandlerOp11.bin", "wb")
pickle.dump(dataToDump, outputFileHandler)
