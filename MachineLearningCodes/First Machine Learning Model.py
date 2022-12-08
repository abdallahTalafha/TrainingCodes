import pandas as pd
from sklearn.tree import DecisionTreeRegressor

melbourne_file_path= "C:/Users/Abdal/Desktop/Python/MachineLearningCodes/melb_data.csv"
melbourne_data = pd.read_csv(melbourne_file_path)

#print(melbourne_data.head())
#print(melbourne_data.columns)
 # dropna drops missing values 
#Selecting The Prediction Target

y=melbourne_data.Price

#Choosing "Features"
#features: The columns that are inputted into our model (and later used to make predictions).

melbourne_features = ['Rooms','Bathroom','Landsize','Lattitude','Longtitude']

X=melbourne_data[melbourne_features]

print(X.describe())
print(X.head())