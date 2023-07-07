import pandas as pd

reviews = pd.read_csv("data\winemag-data_first150k.csv", index_col=0)
"""
print(reviews.keys() )
Index(['Unnamed: 0', 'country', 'description', 'designation', 'points',
       'price', 'province', 'region_1', 'region_2', 'variety', 'winery'],
      dtype='object')
"""

#print(reviews.points.describe() )
#print(reviews.price.describe() )
#print(reviews.loc[:19].price.describe())
#print(reviews.points.mean() )
#print(reviews.loc[10000:50000, ["price", "points"]].describe() )
#print(reviews.country.unique() )
#print(reviews.loc[ reviews.country == "Japan"].variety.unique() )
#print(reviews.country.value_counts() )

"""
review_points_mean = reviews.points.mean()
print(review_points_mean)
the_map = reviews.points.map(lambda p: p - review_points_mean) 
print(sum(the_map))#3.227688694096287e-08 basically zero
"""
"""
for pt in reviews.points:
    print(pt >>2 )
#I can do better
"""
"""
shifted = reviews.points.map(lambda pt: pt >>2)
print(shifted)
#done
"""
"""
#another succesful test
reviews.points = reviews.points.map(lambda pt: pt >>2)
print(reviews)
"""

#countries = reviews.country[~reviews.country.duplicated()] #finds not duplicates
"""
reviews["bargain"] =  reviews.price/reviews.points
print(reviews.sort_values("bargain").iloc[0])
"""
"""
count = reviews.description.map(lambda fr: "tropical" in fr or "fruity" in fr)
print(sum(count))
"""

"""
fruity = sum(reviews.description.map(lambda fr: "fruity" in fr))
tropical = sum(reviews.description.map(lambda fr: "tropical" in fr))
descriptor_counts = pd.Series([tropical, fruity], index=["tropical", "fruity"])
"""
