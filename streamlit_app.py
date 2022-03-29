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
'''
X = df[df.columns]
X = sm.add_constant(X)
y = df['Was_Injured?']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

Injured = df[df['Was_Injured?'] == 1]
Not_Injured = df[df['Was_Injured?'] == 0]

cols = [
       'Age',
       'Work_Rate', '% Games Played When Fit', 'Club_Arsenal',
       'Club_Aston Villa', 'Club_Brighton', 'Club_Burnley', 'Club_Chelsea',
       'Club_Crystal Palace', 'Club_Everton', 'Club_Fulham',
       'Club_Leeds United', 'Club_Leicester City', 'Club_Liverpool FC',
       'Club_Manchester City', 'Club_Manchester United',
       'Club_Newcastle United', 'Club_Sheffield United', 'Club_Southampton',
       'Club_Tottenham Hotspur', 'Club_West Bromwich Albion',
       'Club_West Ham United', 'Club_Wolverhampton Wanderers', 'Best Pos_CM',
       'Best Pos_GK', 'Best Pos_LD', 'Best Pos_LM', 'Best Pos_RD',
       'Best Pos_RM', 'Best Pos_ST', 'Best Pos_CD']

lg_reg = sm.Logit(y_train, X_train[cols])
results = lg_reg.fit()
X_train['target_pred'] = results.predict(X_train[cols])

st.dataframe(data=X_train, width=None, height=None)
'''
