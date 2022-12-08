import pandas as pd

reviews = pd.read_csv("C:/Users/Abdal/Desktop/Python/PandasCodes/winemag.csv", index_col=0)
#pd.set_option('max_rows', 5)

#Native accessors
print(reviews['country'][0])
print(reviews.country)

#Indexing in pandas
#print()
print(reviews.iloc[0])
print(reviews.iloc[:, 0])
print(reviews.iloc[:3, 0])
print(reviews.iloc[1:3, 0])
print(reviews.iloc[[0, 1, 2], 0])
print(reviews.iloc[-5:])
print(reviews.loc[0, 'country'])
print(reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

#Manipulating the index
print(reviews.set_index("title"))

#Conditional selection
print()
print(reviews.country == 'Italy')
print(reviews.loc[reviews.country == 'Italy'])
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])
print(reviews.loc[(reviews.country == 'Italy') | (reviews.points >= 90)])
print(reviews.loc[reviews.country.isin(['Italy', 'France'])])
print(reviews.loc[reviews.price.notnull()])

#Assigning data
reviews['critic'] = 'everyone'
print(reviews['critic'])

reviews['index_backwards'] = range(len(reviews), 0, -1)
print(reviews['index_backwards'])