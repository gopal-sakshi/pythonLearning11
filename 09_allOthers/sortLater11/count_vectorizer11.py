from sklearn.feature_extraction.text import CountVectorizer
corpus = [
    'This is the first document.',
    'This document is the second document.',
    'And this is the third one.',
    'Is this the first document?',
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)
# print(X.toarray())
print("feature names of vectorizer23 ===> ", vectorizer.get_feature_names_out())


vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
X2 = vectorizer2.fit_transform(corpus)
print("feature names of vectorizer24 ===> ", vectorizer2.get_feature_names_out())