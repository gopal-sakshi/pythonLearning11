import pandas as pd

running23 = {
    "time": [8, 10, 15],
    "caloriesSpent": [60, 90, 120]
}

myvar15 = pd.DataFrame(running23, index=['day1', 'day2','day3'])

# print(myvar15)
# print(myvar15.loc[0])
print(myvar15.loc['day2'])
# print(myvar15.loc[[0, 1]])
