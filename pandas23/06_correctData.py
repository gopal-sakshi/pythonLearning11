import pandas as pd

'''
    wrong data ("Duration" in row 7)
    duplicates (row 11 and 12)
    empty cells ("Date" in row 22, "Calories" in row 18 & 28).
    wrong format ("Date" in row 26)
'''
df = pd.read_csv('pandas23/06_pulseData.csv')
# new_df1 = df.dropna()               # returns a new DataFrame, not change the original.
# print(new_df1.to_string())

df.dropna(inplace = True)           ### inplace = changes the original Doc
print(df.to_string())               ### dropna ==> drop all rows with any null value 
                                        ### (see output; row 17, 27 wont be there)
