import streamlit as st
import numpy as np
import pandas as pd
import datetime


dataset = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
df = pd.read_csv(dataset)

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
graph = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

st.dataframe(graph)
st.line_chart(data=graph, width=0, height=0, use_container_width=True)

dataset2 = 'dataset/Players_Combined_Cleaned.csv'
df2 = pd.read_csv(dataset2)
st.dataframe(data=df2, width=None, height=None)


#dataset2= 'https://github.com/DPritchard29/Football-Injury-Predictor---Capstone/blob/master/dataset/Players_Combined_Cleaned.csv'



graph2 = df2.groupby('Best Pos')[['Was_Injured?']].mean().sort_values(['Was_Injured?'], ascending = [False])
st.line_chart(data=graph2, width=0, height=0, use_container_width=True)

