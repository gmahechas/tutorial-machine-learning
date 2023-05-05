import numpy as np
import pandas as pd

from numpy.random import randn

np.random.seed(101)
df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(df)

print(df['W'])
print(type(df))
print(type(df['W']))

df['new'] = df['W'] + df['Y']
print(df)

df.drop('new', axis=1, inplace=True)  # inplace=True means we are modifying the original data frame, axis=1 means we are deleting the column and 0 means we are deleting the row
print(df)
print(df.shape)
print(df.loc['A'])
print(df.iloc[0])
