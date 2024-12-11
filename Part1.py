



#   line chart for total number of steps on daily basis 

import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('dailySteps_merged.csv')

df['ActivityDay'] = pd.to_datetime(df['ActivityDay'])
#  here we group by activity day , bcz its repeated , one activityDay is many times , so we group 
#  by it and use .sum() operation , to calculate total of each activity day 
daily_steps = df.groupby('ActivityDay')['StepTotal'].sum()

plt.figure(figsize=(10, 6))
plt.plot(daily_steps.index, daily_steps.values, marker='o')
plt.title('Total Number of Steps on a Daily Basis')
plt.xlabel('Date')
plt.ylabel('Total Steps')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



#  bar chart for total distance covered



df = pd.read_csv('dailyActivity_merged.csv')
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
daily_distance = df.groupby('ActivityDate')['TotalDistance'].sum()


plt.figure(figsize=(10, 6))
plt.bar(daily_distance.index, daily_distance.values, color='orange')
plt.title('Daily Distance Covered')
plt.xlabel('Date')
plt.ylabel('Distance (km)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#  scatter chart

df = pd.read_csv('sleepDay_merged.csv')
df['SleepDay'] = pd.to_datetime(df['SleepDay'])
time_in_bed = df.groupby('SleepDay')['TotalTimeInBed'].sum()

# Plotting the scatter chart
plt.figure(figsize=(10, 6))
plt.scatter(time_in_bed.index, time_in_bed.values, color='blue')
plt.title('Total Time in Bed')
plt.xlabel('Date')
plt.ylabel('Time in Bed (hours)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#   Draw the Pie chart for the hourly steps on the 12th April 2016. 


df = pd.read_csv('hourlySteps_merged.csv')
df['ActivityHour'] = pd.to_datetime(df['ActivityHour'])

april_12_data = df[df['ActivityHour'].dt.date == pd.to_datetime('2016-04-12').date()]


april_12_hourly_steps = april_12_data.groupby(df['ActivityHour'].dt.hour)['StepTotal'].sum()

plt.figure(figsize=(8, 8))
plt.pie(april_12_hourly_steps.values, labels=april_12_hourly_steps.index, autopct='%1.1f%%')
plt.title('Hourly Steps on 12th April 2016')
plt.show()







