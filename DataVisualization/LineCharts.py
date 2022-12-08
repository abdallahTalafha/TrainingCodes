import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline \\ only if using Jupyter notebook
import seaborn as sns
print('Setup Complete')

spotify_filepath = "C:/Users/Abdal/Desktop/Python/DataVisualization/spotify.csv"
spotify_data = pd.read_csv(spotify_filepath,index_col='Date',parse_dates=True)
print(spotify_data.head())
print(spotify_data.tail())

# Change the style of the figure to the "dark" theme
"""
"darkgrid"
"whitegrid"
"dark"
"white"
"ticks"
"""
sns.set_style("dark")

plt.figure(figsize=(14,6))
plt.title("Daily Global Streams of Popular Songs in 2017-2018")
sns.lineplot(data=spotify_data)
sns.lineplot(data=spotify_data['Shape of You'], label='shape of you')
sns.lineplot(data=spotify_data['Despacito'], label="Despacito")
print(list(spotify_data.columns))
plt.xlabel("Date")
plt.ylabel('Million Plays')
plt.show()