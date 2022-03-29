import streamlit as st
import numpy as np
import pandas as pd
import datetime


dataset = 'dataset/Players_Combined_Cleaned.csv'
df = pd.read_csv(dataset)
st.dataframe(data=df, width=None, height=None)

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

player_info = {"Age": [20],
              "Work_Rate": [15],
              "% Games Played When Fit": [0.8],
              "Club_Arsenal": [0],
              "Club_Aston Villa": [0],
              "Club_Brighton": [0],
              "Club_Burnley": [0],
              "Club_Chelsea": [0],
              "Club_Crystal Palace": [0],
              "Club_Everton": [1],
              "Club_Fulham": [0],
              "Club_Leeds United": [0],
              "Club_Leicester City": [0],
              "Club_Liverpool FC": [0],
              "Club_Manchester City": [0],
              "Club_Manchester United": [0],
              "Club_Newcastle United": [0],
              "Club_Sheffield United": [0],
              "Club_Southampton": [0],
              "Club_Tottenham Hotspur": [0],
              "Club_West Bromwich Albion": [0],
              "Club_West Ham United": [0],
              "Club_Wolverhampton Wanderers": [0],
              "Best Pos_CM": [1],
              "Best Pos_GK": [0],
              "Best Pos_LD": [0],
              "Best Pos_LM": [0],
              "Best Pos_RD": [0],
              "Best Pos_RM": [0],
              "Best Pos_ST": [0],
              "Best Pos_CD": [0]
              }

def injury_calculator(player_info):
    df = pd.DataFrame(player_info)
    df['target_pred'] = results.predict(df[cols])
    if df['target_pred'][0] &gt; 0.75:
        risk = 'High risk'
    elif df['target_pred'][0] &gt; 0.57:
        risk = 'Medium risk'
    else:
        risk = 'Low risk'
    
    expected_games_missed = int(round((2.718**((df['target_pred'][0])*-1))*20, 0))
    print(f'Expected games missed = {expected_games_missed}')
    print(f'This player is = {risk}')

injury_calculator(player_info)
