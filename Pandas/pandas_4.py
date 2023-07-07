import pandas as pd

reviews = pd.read_csv("data\winemag-data_first150k.csv", index_col=0)

#print(reviews.price.dtype) #column type
#print(reviews.dtypes) #ech column type
#print(reviews.points.astype("Float64"))
#print(reviews[pd.isnull(reviews.price)])#gets all the NaN values

#print(reviews.price.fillna(0))
#print(reviews.ffill().groupby("country").country.count()) #already did this one

#print(reviews.price.fillna(method="ffill")) #ffills uses previous value to fill the following if it is a NaN
#print(reviews.price.ffill()) #this does the same as fillna(method="ffill")

"""
nice little detail
reviews.country = reviews.country.replace("Mexico", "México")
print(reviews.groupby("country").country.count())
"""
#print(reviews.price.isnull().sum())
"""
reviews_per_region =  reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
print(reviews_per_region)
"""
#print(reviews.groupby("country").size()) #does the same as reviews.groupby("country").country.count()
#print(reviews.groupby("price").points.max())#this one creates a dataframe for each price, gets the points series(column) of each group and then gets the highest points in each series

"""
#this groups by variety, gets the price column and returns a dataframe with the values on each colmn resulting of applying the functions called by "agg" to the original series
price_extremes = reviews.groupby("variety").price.agg(["min", "max"])
"""
#same as the previous one, but gets the columns (min and max) and sorts in that order
#sorted_varieties = price_extremes.sort_values(by=["min", "max"], ascending=False)

#this generates a double index, counts the values and sorts it in descending order
#country_variety_counts = reviews.groupby(["country", "variety"]).size().sort_values(ascending=False)
