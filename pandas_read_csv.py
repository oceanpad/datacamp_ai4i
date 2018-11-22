import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('notifications.csv')
print df.info()
print df.describe()
print type(df['message_id'].values)
#plt.plot(df['message_id'].values)
#plt.show()
