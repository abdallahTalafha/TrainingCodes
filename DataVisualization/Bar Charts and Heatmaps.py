import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline \\ only if using Jupyter notebook
import seaborn as sns
print('Setup Complete')

flight_filepath ="C:/Users/Abdal/Desktop/Python/DataVisualization/flight_delays.csv"
flight_data = pd.read_csv(flight_filepath, index_col="Month")
print(flight_data)

#Barplot

plt.figure(figsize=(10,6))
plt.title("Average Arrival Delay for Spirit Airlines Flights, by Month")
sns.barplot(x=flight_data.index, y=flight_data['NK'])
plt.ylabel('Arrival delay (in minutes')


#Heatmap
plt.figure(figsize=(14,7))
plt.title("Average Arrival Delay for Each Airline, by Month")
sns.heatmap(data=flight_data,annot= True)
plt.xlabel("Airline")
plt.show()