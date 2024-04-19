import pandas as pd
import numpy as np

running23 = {
    "time": [8, 10, 15],
    "caloriesSpent": [60, 90, 120]
}

myvar15 = pd.DataFrame(running23, index=['day1', 'day2','day3'])

# print(myvar15)
# print(myvar15.loc[0])
print(myvar15.loc['day2'],'\n')
# print(myvar15.loc[[0, 1]])

########################################################################################

df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    # "F": ["foo1","foo2","foo3","foo4","foo5"],                ## ERROR: all arrays must be same length
    "F": ["foo1","foo2","foo3","foo4"],                         ## WORKS: all arrays must be same length
})
print("this is 2nd dataframe =====================> ",'\n')
print(df2["F"])
print(df2["F"][2])
########################################################################################