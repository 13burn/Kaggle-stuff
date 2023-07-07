import pandas as pd

canadian_youtube = pd.read_csv("data\CAvideos.csv")
british_youtube = pd.read_csv("data\GBvideos.csv")

print(canadian_youtube.shape)
print(british_youtube.shape)
print(pd.concat([canadian_youtube, british_youtube]))