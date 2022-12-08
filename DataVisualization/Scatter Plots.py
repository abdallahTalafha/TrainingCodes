import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline \\ only if using Jupyter notebook
import seaborn as sns
print('Setup Complete')

insurance_filepath ="C:/Users/Abdal/Desktop/Python/DataVisualization/insurance.csv"
insurance_data=pd.read_csv(insurance_filepath)
print(insurance_data.head())


#scatterplot
plt.figure(figsize=(10,6))
sns.scatterplot(x=insurance_data['bmi'],y=insurance_data['charges'],hue=insurance_data['smoker'])

#regplot
sns.regplot(x=insurance_data['bmi'],y=insurance_data['charges'])

#lmplot
sns.lmplot(x="bmi", y="charges", hue="smoker", data=insurance_data)
plt.figure(figsize=(10,6))

#swarmplot
sns.swarmplot(x=insurance_data['smoker'],y=insurance_data['charges'])
plt.show()