import pandas as pd
from glob import glob

#filenames = ['sales-jan-2015.csv', 'sales-feb-2015.csv']
filenames = glob('sales*.csv')
dataframes = []

#for f in filenames:
#    dataframes.append(pd.read_csv(f))

dataframes = [pd.read_csv(f) for f in filenames]
print(dataframes)
