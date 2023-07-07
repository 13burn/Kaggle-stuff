import pandas as pd

canadian_youtube = pd.read_csv("data\CAvideos.csv")
british_youtube = pd.read_csv("data\GBvideos.csv")

#print(canadian_youtube.shape)
#print(british_youtube.shape)
#print(pd.concat([canadian_youtube, british_youtube]))

left =  canadian_youtube.set_index(["title", "trending_date"])
right = british_youtube.set_index(["title", "trending_date"])
#print(left)
print(left.join(right, lsuffix="_CAN", rsuffix="_UK") )
