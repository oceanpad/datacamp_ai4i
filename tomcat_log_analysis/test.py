import pandas as pd
import matplotlib.pyplot as plt
import csv
import re
import glob
import seaborn as sns

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

new_df = df.set_index('ts')

#print new_df.head()
#print new_df.describe()
#print new_df.info()
#print new_df.index


df.to_csv('df_csv.csv')

#new_df.plot()
plt.xlable = 'ram'
plt.ylable = 'ts'
#print new_df.head()
#print new_df.keys()
plt.subplot(2,2,1)
plt.plot(new_df)
plt.legend(['all'])

resampled_df = new_df.resample('50T').mean()
plt.subplot(2,2,2)
plt.plot(resampled_df, label='50mins mean')
plt.legend()

resampled_df2 = new_df.resample('50T').std()
plt.subplot(2,2,3)
plt.plot(resampled_df2, label='50mins std')
plt.legend()

print resampled_df

#df.plot(x = 'ts', y = 'ram')
#ram_max = df['ram'].max()
#ts_max = df['ts'][df['ram'].argmax()]
# Add a black arrow annotation
#plt.annotate('Max', xy=(ts_max, ram_max), xytext=(ts_max, ram_max+2),arrowprops=dict(facecolor='black'))


#sns.pairplot(df, kind='reg')

fig1 = plt.gcf()
plt.show()
fig1.savefig('tomcat.png', dpi=300)
