import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline \\ only if using Jupyter notebook
import seaborn as sns
#print('Setup Complete')

iris_filepath ="C:/Users/Abdal/Desktop/Python/DataVisualization/iris.csv"
iris_data=pd.read_csv(iris_filepath)
print(iris_data.head())

#Histograms
sns.histplot(iris_data['Petal Length (cm)'])

#Density plots
#(KDE) kernel density estimate 
sns.kdeplot(data=iris_data['Petal Length (cm)'],shade= True)
sns.kdeplot(data=iris_data, x='Petal Length (cm)', hue='Species', shade=True)

#2D KDE plots
#2D KDE two-dimensional KDE plot
sns.jointplot(x=iris_data['Petal Length (cm)'], y=iris_data['Sepal Width (cm)'], kind="kde")

#Color-coded plots
#histplot
sns.histplot(data=iris_data,x='Petal Length (cm)',hue='Species')
plt.title("Histogram of Petal Lengths, by Species")
plt.show()
