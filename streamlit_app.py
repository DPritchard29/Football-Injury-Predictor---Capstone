import streamlit as st
import numpy as np
import pandas as pd
import datetime

age = st.slider('Age', min_value = 18, max_value = 28)
work_rate = st.slider('Work Rate', min_value = 0, max_value = 20)

player_info = {"Age": age,
              "Work_Rate": work_rate,
              "% Games Played When Fit": 0.514286,
              "Club_Arsenal": 0,
              "Club_Aston Villa": 0,
              "Club_Brighton": 0,
              "Club_Burnley": 0,
              "Club_Chelsea": 0,
              "Club_Crystal Palace": 0,
              "Club_Everton": 0,
              "Club_Fulham": 0,
              "Club_Leeds United": 0,
              "Club_Leicester City": 0,
              "Club_Liverpool FC": 0,
              "Club_Manchester City": 0,
              "Club_Manchester United": 0,
              "Club_Newcastle United": 1,
              "Club_Sheffield United": 0,
              "Club_Southampton": 0,
              "Club_Tottenham Hotspur": 0,
              "Club_West Bromwich Albion": 0,
              "Club_West Ham United": 0,
              "Club_Wolverhampton Wanderers": 0,
              "Best Pos_CM": 0,
              "Best Pos_GK": 0,
              "Best Pos_LD": 0,
              "Best Pos_LM": 1,
              "Best Pos_RD": 0,
              "Best Pos_RM": 0,
              "Best Pos_ST": 0,
              "Best Pos_CD": 0
              }



pred_calc = (2.71828 ** (0.001416+ (0.0473*player_info['Age'])+ (0.0742*player_info['Work_Rate'])+ (1.6308*player_info['% Games Played When Fit'])- (0.1082*player_info['Club_Arsenal'])- (1.7763*player_info['Club_Aston Villa'])- (0.8425*player_info['Club_Brighton'])+ (0.0778*player_info['Club_Burnley'])- (0.2886*player_info['Club_Chelsea'])- (0.8169*player_info['Club_Crystal Palace'])- (0.1118*player_info['Club_Everton'])- (1.0453*player_info['Club_Fulham'])- (1.5009*player_info['Club_Leeds United'])- (0.6155*player_info['Club_Leicester City'])+ (0.0972*player_info['Club_Liverpool FC'])- (0.1572*player_info['Club_Manchester City'])- (0.5927*player_info['Club_Manchester United'])- (0.1186*player_info['Club_Newcastle United'])- (1.1161*player_info['Club_Sheffield United'])- (0.7287*player_info['Club_Southampton'])- (0.2732*player_info['Club_Tottenham Hotspur'])- (2.3910*player_info['Club_West Bromwich Albion'])+ (0.0206*player_info['Club_West Ham United'])- (1.2760*player_info['Club_Wolverhampton Wanderers'])- (2.0324*player_info['Best Pos_CM'])- (2.4456*player_info['Best Pos_GK'])- (0.8274*player_info['Best Pos_LD'])- (1.3731*player_info['Best Pos_LM'])- (1.7715*player_info['Best Pos_RD'])- (1.7552*player_info['Best Pos_RM'])- (2.1189*player_info['Best Pos_ST'])- (1.2397*player_info['Best Pos_CD']))) / (1+ (2.71828 ** (0.001416+ (0.0473*player_info['Age'])+ (0.0742*player_info['Work_Rate'])+ (1.6308*player_info['% Games Played When Fit'])- (0.1082*player_info['Club_Arsenal'])- (1.7763*player_info['Club_Aston Villa'])- (0.8425*player_info['Club_Brighton'])+ (0.0778*player_info['Club_Burnley'])- (0.2886*player_info['Club_Chelsea'])- (0.8169*player_info['Club_Crystal Palace'])- (0.1118*player_info['Club_Everton'])- (1.0453*player_info['Club_Fulham'])- (1.5009*player_info['Club_Leeds United'])- (0.6155*player_info['Club_Leicester City'])+ (0.0972*player_info['Club_Liverpool FC'])- (0.1572*player_info['Club_Manchester City'])- (0.5927*player_info['Club_Manchester United'])- (0.1186*player_info['Club_Newcastle United'])- (1.1161*player_info['Club_Sheffield United'])- (0.7287*player_info['Club_Southampton'])- (0.2732*player_info['Club_Tottenham Hotspur'])- (2.3910*player_info['Club_West Bromwich Albion'])+ (0.0206*player_info['Club_West Ham United'])- (1.2760*player_info['Club_Wolverhampton Wanderers'])- (2.0324*player_info['Best Pos_CM'])- (2.4456*player_info['Best Pos_GK'])- (0.8274*player_info['Best Pos_LD'])- (1.3731*player_info['Best Pos_LM'])- (1.7715*player_info['Best Pos_RD'])- (1.7552*player_info['Best Pos_RM'])- (2.1189*player_info['Best Pos_ST'])- (1.2397*player_info['Best Pos_CD']))))

def risk_calc(pred_calc):
  if pred_calc > 0.75:
    return 'High risk'
  elif pred_calc > 0.57:
    return 'Medium risk'
  else:
    return 'Low risk'

def expected_games_missed(pred_calc):
  expected_games_missed = int(round((2.718**((pred_calc)*8))*0.02,0))
  return expected_games_missed
  
  
  
st.text(player_info['Age'])
st.text(pred_calc)
st.text(risk_calc(pred_calc))
st.text(expected_games_missed(pred_calc))
