import pandas as pd
import numpy as np
df = pd.read_csv('09_allOthers/sortLater11/ted11.csv')

# print("head ===========> ", df.head())              ## print top 5 rows
# print("columns =========> ", df.dtypes)             ## print column names of csv

ted = df['description']
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()                      # Create TfidfVectorizer object
tfidf_matrix = vectorizer.fit_transform(ted)        # Generate matrix of word vectors
print("matrix23 shape ===>", tfidf_matrix.shape)    # Print the shape of tfidf_matrix