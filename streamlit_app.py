import streamlit as st
import numpy as np
import pandas as pd
import datetime

'''
dataset2 = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
df2 = pd.read_csv(dataset2)

df2['Order Date'] = pd.to_datetime(df2['Order Date'], format='%m/%d/%Y')
graph2 = df2.groupby(df2['Order Date'].dt.month)['Sales'].sum()

st2.dataframe(graph2)
st.line_chart(data=graph2, width=0, height=0, use_container_width=True)
'''


dataset = 'dataset/Players_Combined_Cleaned.csv'
df = pd.read_csv(dataset)
st.dataframe(data=df, width=None, height=None)
