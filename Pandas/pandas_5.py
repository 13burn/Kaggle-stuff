import pandas as pd

reviews = pd.read_csv("data\winemag-data_first150k.csv", index_col=0)

#reviews.rename(columns={"points":"score"}, inplace=True)#without "inplace" creates a new copy of the dataframe witht the modified column name
#reviews.rename(index={0:"First Entry", 1:"Second entry"}, inplace=True)

"""
THIS WILL NOT WORK
if a dataframe has to be modified in place this will not work
reviews.rename_axis("wines", axis="rows", inplace=True).rename_axis("fields", axis="columns",  inplace=True)

#this will work, most likely the first call is not parsing the updated DataFrame, need to check the docs to understand why, but this works
reviews.rename_axis("wines", axis="rows", inplace=True)
reviews.rename_axis("fields", axis="columns",  inplace=True)
"""


print(reviews)