import streamlit as st
import numpy as np
import pandas as pd
import datetime
import os

dataset = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
df = pd.read_csv(dataset)

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
graph = df.groupby(df['Order Date'].dt.month)['Sales'].sum()

st.dataframe(graph)
st.line_chart(data=graph, width=0, height=0, use_container_width=True)
