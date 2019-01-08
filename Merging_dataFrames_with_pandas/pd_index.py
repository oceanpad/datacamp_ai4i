import pandas as pd
w_mean = pd.read_csv('pittsburgh2013.csv', index_col='Date')
w_max = pd.read_csv('pittsburgh2013.csv', index_col='Date')
print(w_mean.head())
print(w_max.head())

print(w_mean.index)
print(w_max.index)

w_mean.sort_index()
w_max.sort_index()

print(w_mean.head())
print(w_max.head())

w_mean.reindex(w_max.index)
print(w_mean.head())


weather = pd.read_csv('pittsburgh2013.csv', index_col='Date', parse_dates=True)

print(weather.loc['2013-07-01':'2013-07-07', 'PrecipitationIn'] * 2.54)

week1_range = weather.loc['2013-07-01':'2013-07-07', ['Min TemperatureF', 'Max TemperatureF']]
print(week1_range)

week1_mean = weather.loc['2013-07-01':'2013-07-07', 'Mean TemperatureF']
print(week1_mean)

result = week1_range.divide(week1_mean, axis='rows')
print(result)

pct = week1_mean.pct_change() * 100
print(pct)

all_range = weather.loc[:, ['Min TemperatureF', 'Max TemperatureF']]
pct2 = all_range.pct_change() * 100
print(pct2)
