import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline \\ only if using Jupyter notebook
import seaborn as sns
print('Setup Complete')

fifa_filepath = "fifa.csv"
fifa_data = pd.read_csv(fifa_filepath, index_col="Date", parse_dates=True)
print(fifa_data.head())

plt.figure(figsize=(16,6))
sns.lineplot(data=fifa_data)
plt.show()