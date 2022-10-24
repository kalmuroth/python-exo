import numpy as np
import pandas as pd
import seaborn as sns
import os
import gc

read = pd.read_csv("C:/Users/lucas/OneDrive/Bureau/serpent/input/sales_predictions.csv").sample(n=50, random_state=1)
#read = pd.to_datetime(read["date"], format='%d%m%Y')
test = sns.relplot(data=read, x="date", y="item_price")
print(test)