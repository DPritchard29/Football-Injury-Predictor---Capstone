import streamlit as st
import pandas as pd

dataset = 'https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv'
df = pd.read_csv(dataset)

st.dataframe(df)

st.line_chart(data=df, x = 'Row ID', y = 'Sales')
