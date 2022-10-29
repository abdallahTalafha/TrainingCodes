import pandas as pd


a = [1, 7, 2]

myvar1 = pd.Series(a, index = ["x", "y", "z"])

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2] 
}

myvar2 = pd.DataFrame(mydataset)
pd.options.display.max_rows


print(myvar1)
#print(myvar2)