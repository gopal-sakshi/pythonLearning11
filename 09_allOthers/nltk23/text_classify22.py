import text_classify21 as file1
import numpy as np

word_features = [x[0] for x in file1.all_words.most_common(15)]
# word_features ====> ['film', 'movie', 'one', 'character', ... 1500 items]

def find_features(words):
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return np.array(list(features.values()))

## columns represent 'words' & values are 'binary values' representing the presence of that word in a review.
### feature_vector ---> 2000 rows, 15 columns       
    # 1st row ==> 1st pos review, 2nd row ===> 2nd pos review, 
    # 1001 row ===> 1st neg review and so on...
    # 1st column ===> presence of word 'film' 
    # 2nd column ===> presence of word 'movie'
    # 4th column ===> presence of word 'character'

## https://www.projectpro.io/article/nltk/846
feature_vector = np.array([find_features(s) for s in file1.df['text'].values])

y = file1.df['label'].values
print("feature_vector =============> ", feature_vector)
print("shapes =============> ", feature_vector.shape, y.shape)
