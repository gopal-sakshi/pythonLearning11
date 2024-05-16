import spacy
nlp = spacy.load("en_core_web_sm")

# print("list of strings ===>", list(nlp.vocab.strings))
print("length of that list======>", len(list(nlp.vocab.strings)))