import pandas as pd

df = pd.read_csv('pandas23/06_pulseData.csv')
# print(df)
# print(df.columns)

### WONT PERSIST
# new_df = df.drop(['Index23'], axis=1)
# print(new_df)
# print(new_df.columns)

### PERSIST
df = df.drop(['Index23'], axis=1,inplace=True)