https://github.com/shaadclt/Future-Sales-Prediction-LinearRegression

Historical data on advertising expenditures & corresponding sales for different channels. 

TV:         Advertising budget for TV in thousands of dollars.
Radio:      Advertising budget for radio in thousands of dollars.
Newspaper:  Advertising budget for newspaper in thousands of dollars.
Sales:      Sales in thousands of units.

`Linear regression`
- statistical approach 
- model the relationship between a dependent variable (sales) and independent variables (TV, radio, newspaper)
- train the model based on 160 rows <train set>
- predict the "sales" value for next corresponding 40 rows <test set>
- use "mean_squared_error" <MSE> to compare "predictionValues" & "actualValues" for those 40 rows <test set>
- the lower the <MSE value> the better and 0 means the model is perfect.

Mean squared error
- square the difference between <actual> and <forecast> value
- average of all such squares