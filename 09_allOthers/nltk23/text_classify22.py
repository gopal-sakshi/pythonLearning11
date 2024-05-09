import text_classify21 as file1
import numpy as np

word_features = [x[0] for x in file1.all_words.most_common(1500)]

def find_features(words):
    features = {}
    for word in word_features:
        features[word] = (word in words)
    return np.array(list(features.values()))

feature_vector = np.array([find_features(s) for s in file1.df['text'].values])

y = file1.df['label'].values
print("shapes =============> ", feature_vector.shape, y.shape)