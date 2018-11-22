import pandas as pd
import matplotlib.pyplot as plt
import csv
import re
import glob

csv_files = glob.glob('*.log')
csv_str = ''
for filename in csv_files:
  used = [ line for line in open(filename) if ' used' in line]

  for line in used:
    ram = re.search('GB\((.*)\%\)', line)
    datetime = re.search('(.*) INFO', line)
    csv_str += ram.group(1) + ',' + datetime.group(1)[:20] + '\n'


with open('test.csv', 'wb') as myfile:
    myfile.write(csv_str)

df = pd.read_csv('test.csv', delimiter=',', header = None)
df.columns = ['ram', 'ts']
df.ts=pd.to_datetime(df.ts)

print df.head()
print df.describe()
print df.info()

df.to_csv('df_csv.csv')

df.plot(x = 'ts', y = 'ram')
plt.xlable = 'ram'
plt.ylable = 'ts'
plt.show()

