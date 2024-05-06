from sklearn.feature_extraction.text import TfidfVectorizer
corpus = [
    'The car runs on the road',
    'The ship sails on water',
    'Aeroplane flies in air',
    'Pedestrians must walk on sideway',
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(corpus)
vectorizer.get_feature_names_out()
print(X.shape)