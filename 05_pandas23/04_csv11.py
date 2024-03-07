import pandas as pd

df11 = pd.read_csv('pandas23/04_currency.csv')

print(pd.options.display.max_rows)          ### if data contains more than 60 rows, pandas prints first & last 5 rows


# print(df11)
# print(df11.to_string)               ## whats the difference to_string vs to_string()
print(df11.to_string())