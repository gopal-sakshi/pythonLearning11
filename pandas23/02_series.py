import pandas as pd

a = [1, 7, 2]
myvar11 = pd.Series(a)        ## series === like a column in a table (or) 1D array
print(myvar11,'\n')                    ### here labels will be 0,1,2

players12 = ['Kaka', 'Casillas', 'PEpe', 'Xabi']
myvar12 = pd.Series(players12, index=['pl1', 'pl2', 'pl3', 'pl4'])
print(myvar12,end='\n____kotha___line23____\n')


calories = { "day1": 420, "day2": 380, "day3": 390 }
myvar13 = pd.Series(calories)
print(myvar13)

myvar13_onlySome = pd.Series(calories, index = ["day1", "day2"])
print(myvar13_onlySome)