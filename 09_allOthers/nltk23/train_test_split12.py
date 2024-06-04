# import packages
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error



#### 211 rows + 1 row heading of data
df = pd.read_csv('09_allOthers/nltk23/train_advertising.csv')   
# dropping rows which have null values ----> after dropping null values ===> we get 200 rows of valid data
df.dropna(inplace=True,axis=0)


#### "sales" column         ======> y
#### "all_other_columns"    ======> X
y = df['sales']
X = df.drop('sales',axis=1)

# splitting the dataframe into train and test sets 
    # (0.2 means ===> X_train = 160 rows; X_test = 40 rows)
    # (0.05 means ===> X_train = 190 rows; X_test = 10 rows)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=101)
print("X_train length ====> ", len(X_train))
print("X_test length ====> ", len(X_test))
# print("columns of y_test ===> ", list(y_test))
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

model = LinearRegression().fit(X_train,y_train)
y_pred = model.predict(X_test)
print("prediction sales for those 10 rows =====> ", y_pred)
print("actual sales for those 10 rows =========> ", y_test.to_string(index=False))
print("mean squared error ====> ", mean_squared_error(y_test,y_pred))
