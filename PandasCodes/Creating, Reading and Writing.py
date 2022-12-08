import pandas as pd


#Creating data

#DataFrames
data1=pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})

data2=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

data3=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],'Sue': ['Pretty good.', 'Bland.']},index=['Product A', 'Product B'])

#Series
ser1=pd.Series([1, 2, 3, 4, 5])
ser2=pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')


#Reading data files

wine_reviews = pd.read_csv("C:/Users/Abdal/Desktop/Python/PandasCodes/winemag.csv",index_col=0)
print(wine_reviews.head())
print(wine_reviews.shape)

