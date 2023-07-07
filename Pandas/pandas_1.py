import pandas as pd

reviews = pd.read_csv("data\winemag-data_first150k.csv")
#pd.set_option("display.max_rows", 5) #i dont need it right now

#print(reviews.head())
desc = reviews.description #description list
#print(desc)

first_desc = desc.iloc[0] #first description
#print(first_desc)

first_review = reviews.iloc[0] #first review
#print(first_review)

first_descriptions = reviews = reviews.description.iloc[:10]
print(first_descriptions)
