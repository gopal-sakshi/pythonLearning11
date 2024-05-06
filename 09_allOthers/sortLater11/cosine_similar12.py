corpus = ['The sun is the largest celestial body in the solar system', 
          'The solar system consists of the sun and eight revolving planets', 
          'Ra was the Egyptian Sun God', 
          'The Pyramids were the pinnacle of Egyptian architecture', 
          'The quick brown fox jumps over the lazy dog']


from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer()                        # Initialize an instance of tf-idf Vectorizer
tfidf_matrix = tfidf_vectorizer.fit_transform(corpus)       # Generate the tf-idf vectors for the corpus
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)  # compute & print the cosine similarity matrix
print("cosine sim ===> ", cosine_sim)