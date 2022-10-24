import numpy as np
import pandas as pd
import seaborn as sns
import streamlit as st
import os
import gc

read = pd.read_csv("sales_predictions.csv").sample(n=50, random_state=1)
test = sns.relplot(data=read, x="date", y="item_price")
st.pyplot(test)