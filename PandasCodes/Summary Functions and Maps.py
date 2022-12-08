import pandas as pd

reviews = pd.read_csv("C:/Users/Abdal/Desktop/Python/PandasCodes/winemag.csv", index_col=0)

#Summary functions

#print(reviews.points.describe())
#print(reviews.points.mean())
#print()
#print(reviews.taster_name.unique())
#print(reviews.taster_name.value_counts())

#Maps

review_points_mean = reviews.points.mean()
#print(reviews.points.map(lambda p: p - review_points_mean))
countries =reviews.country.unique() #countries are represented with no duplicates
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

#print(reviews.apply(remean_points, axis='columns'))
print(reviews.country + " - " + reviews.region_1)
print(reviews.head(1))