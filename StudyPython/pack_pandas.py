
import pandas as pd

# making dataframe
# df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
df = pd.read_csv("D:\EL710\p-Python\sheet.csv", sep=';')

# df.head(x) gives x rows of data, default - the first 5-rows
print(df.head())

print(df.shape)

print(df.dtypes)

cols = df.columns[:1]
print(cols)

print(df[cols].isnull())
