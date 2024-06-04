# Import packages
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import mean_squared_error


# Load the data
irisData = load_iris()

# Create feature and target arrays
X = irisData.data
y = irisData.target

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state=42)

knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(X_train, y_train)

# predicting on the X_test data set
y_pred = knn.predict(X_test)
print("prediction results ====> ", y_pred)
print("actual results ========> ", y_test)
print("mean squared error ====> ", mean_squared_error(y_test, y_pred))
