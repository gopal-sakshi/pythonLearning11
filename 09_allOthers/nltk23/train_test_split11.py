import numpy as np
from sklearn.model_selection import train_test_split

# train_test_split = Split arrays or matrices into random train and test subsets.



X, y = np.arange(10).reshape((5, 2)), range(5)
print("X ===> ",X)
print("y ===>", list(y))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2; 20% of data for test set & 80% for training set

print("X_train ====> ", X_train)
print("y train ====> ", y_train)
print("X_test =====> ", X_test)
print("y_test =====> ", y_test)


# https://www.geeksforgeeks.org/how-to-split-the-dataset-with-scikit-learns-train_test_split-function/
# https://builtin.com/data-science/train-test-split