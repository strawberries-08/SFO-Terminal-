#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

# Load the dataset
df = pd.read_csv('Air_Traffic_Passenger_Statistics.csv')

# Display the first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())
# Convert the 'Activity Period' to datetime
df['Activity Period'] = pd.to_datetime(df['Activity Period'], format='%Y%m')

# Filter for terminal-related data
terminal_data = df[df['Terminal'].notnull()]

# Group by terminal and month to get monthly passenger counts
monthly_passengers = terminal_data.groupby(['Activity Period', 'Terminal'])['Passenger Count'].sum().reset_index(


# In[21]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.dates as mdates
import matplotlib.ticker as ticker

# Convert 'Activity Period' to datetime
monthly_passengers['Activity Period'] = pd.to_datetime(monthly_passengers['Activity Period'])

plt.figure(figsize=(14, 7))

sns.lineplot(data=monthly_passengers, x='Activity Period', y='Passenger Count', hue='Terminal')

# Format x-axis: show one tick per year
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

# Format y-axis: show values in millions
plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: f'{x/1_000_000:.1f}M'))

# Customize the plot
plt.title('Yearly Passenger Traffic by Terminal at SFO')
plt.xlabel('Year')
plt.ylabel('Passenger Count (Millions)')
plt.legend(title='Terminal')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

