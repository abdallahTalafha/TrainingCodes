import pandas as pd

data ={'Yes' : [50,21], 'No' : [131,2]}
data2=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']},index=['Product A','Product B'])

data1=pd.DataFrame(data)
ser1 =pd.Series([1,2,3,4,5])
ser2 =pd.Series([30,35,40],index=['2015 Sales','2016 Sales','2017 Sales'], name='Product A')
data_reviews =pd.read_csv('winemag.csv',index_col=0)

print(data1)
"""
print(data2)
print(ser1)
print(ser2)
"""
#print(data_reviews.shape)
#print(data_reviews.head())









#data_reviews =pd.read_excel('C:\Users\Abdal\Desktop\Python\PandasCodes\UK Agriculture.xlsx')
#data_reviews.head()
#pd.set_option('max_rows', 5)
#dat_reviews.England+
