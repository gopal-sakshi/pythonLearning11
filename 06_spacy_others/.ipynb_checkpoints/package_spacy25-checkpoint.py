import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_md")       


sent23 = nlp('Last Thursday, Manchester United defeated AC Milan at San Siro.')

# POS-Tagging — (Part Of Speech)
    # pos23 ---> ADJ, PUNC, PROPN, VERB, ADP
    # tag23 ---> JJ, NNP, VBD
# NER-Tagging — (Named Entity Recognition)
    # locate and classify unstructured text ---> person name; organization name; location; quantities
# Dependency Parsing
    # examine the dependencies between phrases of a sentence

######################################################################################
for token in sent23:
    # print("text23 ---> ", token.text, "__pos23 ----> ", token.pos_, "__tag23 --->", token.tag_)           ## POS tagging
    print("text23 ---> ", token.text, "____entity type____ ", token.ent_type_)                              ## NER tagging

for chunk in sent23.noun_chunks:
    print('__cT__', chunk.text, '__rt__', chunk.root.text, '__dep__', chunk.root.dep_, '__text__', chunk.root.head.text)        ## Dependency Parsing

for token in sent23:
    # print('_txt_', token.text, '_dep_', token.dep_, token.head.text, token.head.pos_, [child for child in token.children])                ### dependency parsing
    print(token.text, token.dep_, token.head.text, token.head.pos_, [child for child in token.children])                ### dependency parsing

displacy.render(sent23, style='dep', jupyter=True, options={'distance':90})
######################################################################################