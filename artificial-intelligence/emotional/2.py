import pandas as pd
import numpy as np

keyfacial_df = pd.read_csv(
    '/Users/tavogus/resources/python/tutorial-machine-learning/artificial-intelligence/emotional/data.csv')

# print(keyfacial_df.info())

# check if there is null values in dataset
# print(keyfacial_df.isnull().sum())

# Obtain the Shape of the image
# print(keyfacial_df['Image'].shape)
keyfacial_df['Image'] = keyfacial_df['Image'].apply(lambda x: np.fromstring(x, dtype=int, sep=' ').reshape(96, 96))
# print(keyfacial_df['Image'][0].shape)

# describe
print(keyfacial_df.describe())
