import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(f"text23 ==> {token.text}, pos23 ==> {token.pos_}, dep23 ==> {token.dep_}")


'''     HOW TO RUN

python3 -m pip install spacy
python3 -m spacy download en_core_web_sm
    Successfully installed en-core-web-sm-3.7.1
    ✔ Download and installation successful
    You can now load the package via spacy.load('en_core_web_sm')
    ===> it seems that "en_core_web_sm" model is downloaded somewhere in /home/gsakshi/.local/lib/python3.10/site-packages/spacy
python3 package_spacy23.py
'''