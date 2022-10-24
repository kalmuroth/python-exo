import numpy as np
import pandas as pd
import seaborn as sns
import os
import gc

path = os.path.abspath("input/sales_predictions.csv")

read = pd.read_csv(path).sample(n=50, random_state=1)
#read = pd.to_datetime(read["date"], format='%d%m%Y')
test = sns.relplot(data=read, x="date", y="item_price")
print(test)