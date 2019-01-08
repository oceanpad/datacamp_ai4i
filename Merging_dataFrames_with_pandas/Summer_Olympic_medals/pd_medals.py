import pandas as pd

bronze = pd.read_csv('bronze_top5.csv', index_col=0)
print(bronze)

silver = pd.read_csv('silver_top5.csv', index_col=0)
print(silver)

gold = pd.read_csv('gold_top5.csv', index_col=0)
print(gold)

bs = bronze + silver
print(bs)

bs2 = bronze.add(silver, fill_value=0)
print(bs2)

bsg = bronze.add(silver, fill_value=0).add(gold, fill_value=0)
print(bsg)
