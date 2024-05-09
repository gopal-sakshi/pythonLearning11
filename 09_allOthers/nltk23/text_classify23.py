# machine learning models
    # k nearest neighbours
    # decision tree
    # random forest
    # logistic regression
    # support vector machine

##########################################################
import text_classify22 as file2
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, train_test_split
import numpy as np

classifiers = [
    KNeighborsClassifier(),
    DecisionTreeClassifier(),
    RandomForestClassifier(),
    LogisticRegression(),
    SGDClassifier(max_iter=100),
    SVC(kernel='linear')
]

params_dict = [
    dict(n_neighbors=[5,10,25,35,50]),
    dict(max_depth=[5,10,15]),
    dict(n_estimators=[200,400,600,800], max_depth=[5,10]),
    dict(C=[0.05, 0.1,0.5,1.0], penalty=['l2'], max_iter=[500,1000,1500]),
    dict(max_iter=[200,500,1000,1500]),
    dict(kernel=['linear','sigmoid', 'poly','rbf'])
]

names = [
    'KNN', 
    'Decision Tree', 
    'Random Forest', 
    'Logistic Regression', 
    'SGC Classifier', 
    'SVM'
]

X_train, X_test, y_train, y_test = train_test_split(file2.feature_vector, file2.y, test_size=0.2, random_state=42)

for name, params, model in zip(names, params_dict, classifiers):
    clf = GridSearchCV(model, params)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(" ===> ", name, "__", clf.best_params_, "__mean__", np.mean(y_test==y_pred))