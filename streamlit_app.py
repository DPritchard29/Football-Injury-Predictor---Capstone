import streamlit as st
import numpy as np
import pandas as pd

st.header('Welcome to the football player injury predictor!')

club_select = st.selectbox('Select a club you are recruiting for:',
                           ('Arsenal',
                            'Aston Villa',
                            'Brighton',
                            'Burnley',
                            'Chelsea',
                            'Crystal Palace',
                            'Everton',
                            'Fulham',
                            'Leeds',
                            'Leicester',
                            'Liverpool',
                            'Manchester City',
                            'Manchester United',
                            'Newcastle',
                            'Sheffield United',
                            'Southampton',
                            'Tottenham',
                            'West Bromwich Albion',
                            'West Ham',
                            'Wolverhampton Wanderers'))


age = st.slider("Select the player's age",
                min_value = 18,
                max_value = 28)

work_rate = st.slider("Select the player's work rate",
                      min_value = 0,
                      max_value = 20)

position_select = st.selectbox("Select the player's position",
                           ('Goalkeeper',
                            'Left Defense',
                            'Centre Defense',
                            'Right Defense',
                            'Left Midfield',
                            'Centre Midfield',
                            'Right Midfield',
                            'Striker'))

player_importance_select = st.selectbox('How important the the club will the player be?',
                                        ('Star Player',
                                         'First Team',
                                         'Rotation',
                                         'Sporadic',
                                         'Backup'))


player_importance = {'Star Player': 0.9,
                            'First Team': 0.7,
                            'Rotation': 0.5,
                            'Sporadic': 0.3,
                            'Backup': 0.1}

player_info = {"Age": age,
              "Work_Rate": work_rate,
              "% Games Played When Fit": player_importance[player_importance_select],
              "Club_Arsenal": 0,
              "Club_Aston Villa": 0,
              "Club_Brighton": 0,
              "Club_Burnley": 0,
              "Club_Chelsea": 0,
              "Club_Crystal Palace": 0,
              "Club_Everton": 0,
              "Club_Fulham": 0,
              "Club_Leeds": 0,
              "Club_Leicester": 0,
              "Club_Liverpool": 0,
              "Club_Manchester City": 0,
              "Club_Manchester United": 0,
              "Club_Newcastle": 0,
              "Club_Sheffield United": 0,
              "Club_Southampton": 0,
              "Club_Tottenham": 0,
              "Club_West Bromwich Albion": 0,
              "Club_West Ham": 0,
              "Club_Wolverhampton Wanderers": 0,
              "Best Pos_CM": 0,
              "Best Pos_GK": 0,
              "Best Pos_LD": 0,
              "Best Pos_LM": 0,
              "Best Pos_RD": 0,
              "Best Pos_RM": 0,
              "Best Pos_ST": 0,
              "Best Pos_CD": 0}

def position_transform(position_select):
  if position_select == 'Goalkeeper':
    return 'Best Pos_GK'
  elif position_select == 'Left Defense':
    return 'Best Pos_LD'
  elif position_select == 'Centre Defense':
    return 'Best Pos_CD'
  elif position_select == 'Right Defense':
    return 'Best Pos_RD'
  elif position_select == 'Left Midfield':
    return 'Best Pos_LM'
  elif position_select == 'Centre Midfield':
    return 'Best Pos_CM'
  elif position_select == 'Right Midfield':
    return 'Best Pos_RM'
  else:
    return 'Best Pos_ST'

  

player_info[position_transform(position_select)] = 1 
player_info['Club_' + club_select] = 1 

pred_calc = (2.71828 ** (0.001416+ (0.0473*player_info['Age'])+ (0.0742*player_info['Work_Rate'])+ (1.6308*player_info['% Games Played When Fit'])- (0.1082*player_info['Club_Arsenal'])- (1.7763*player_info['Club_Aston Villa'])- (0.8425*player_info['Club_Brighton'])+ (0.0778*player_info['Club_Burnley'])- (0.2886*player_info['Club_Chelsea'])- (0.8169*player_info['Club_Crystal Palace'])- (0.1118*player_info['Club_Everton'])- (1.0453*player_info['Club_Fulham'])- (1.5009*player_info['Club_Leeds'])- (0.6155*player_info['Club_Leicester'])+ (0.0972*player_info['Club_Liverpool'])- (0.1572*player_info['Club_Manchester City'])- (0.5927*player_info['Club_Manchester United'])- (0.1186*player_info['Club_Newcastle'])- (1.1161*player_info['Club_Sheffield United'])- (0.7287*player_info['Club_Southampton'])- (0.2732*player_info['Club_Tottenham'])- (2.3910*player_info['Club_West Bromwich Albion'])+ (0.0206*player_info['Club_West Ham'])- (1.2760*player_info['Club_Wolverhampton Wanderers'])- (2.0324*player_info['Best Pos_CM'])- (2.4456*player_info['Best Pos_GK'])- (0.8274*player_info['Best Pos_LD'])- (1.3731*player_info['Best Pos_LM'])- (1.7715*player_info['Best Pos_RD'])- (1.7552*player_info['Best Pos_RM'])- (2.1189*player_info['Best Pos_ST'])- (1.2397*player_info['Best Pos_CD']))) / (1+ (2.71828 ** (0.001416+ (0.0473*player_info['Age'])+ (0.0742*player_info['Work_Rate'])+ (1.6308*player_info['% Games Played When Fit'])- (0.1082*player_info['Club_Arsenal'])- (1.7763*player_info['Club_Aston Villa'])- (0.8425*player_info['Club_Brighton'])+ (0.0778*player_info['Club_Burnley'])- (0.2886*player_info['Club_Chelsea'])- (0.8169*player_info['Club_Crystal Palace'])- (0.1118*player_info['Club_Everton'])- (1.0453*player_info['Club_Fulham'])- (1.5009*player_info['Club_Leeds'])- (0.6155*player_info['Club_Leicester'])+ (0.0972*player_info['Club_Liverpool'])- (0.1572*player_info['Club_Manchester City'])- (0.5927*player_info['Club_Manchester United'])- (0.1186*player_info['Club_Newcastle'])- (1.1161*player_info['Club_Sheffield United'])- (0.7287*player_info['Club_Southampton'])- (0.2732*player_info['Club_Tottenham'])- (2.3910*player_info['Club_West Bromwich Albion'])+ (0.0206*player_info['Club_West Ham'])- (1.2760*player_info['Club_Wolverhampton Wanderers'])- (2.0324*player_info['Best Pos_CM'])- (2.4456*player_info['Best Pos_GK'])- (0.8274*player_info['Best Pos_LD'])- (1.3731*player_info['Best Pos_LM'])- (1.7715*player_info['Best Pos_RD'])- (1.7552*player_info['Best Pos_RM'])- (2.1189*player_info['Best Pos_ST'])- (1.2397*player_info['Best Pos_CD']))))

def risk_calc(pred_calc):
  if pred_calc > 0.75:
    return 'Risk of injury: High risk'
  elif pred_calc > 0.57:
    return 'Risk of injury: Medium risk'
  else:
    return 'Risk of injury: Low risk'

def expected_games_missed(pred_calc):
  expected_games_missed = int(round((2.718**((pred_calc)*8))*0.02,0))
  return expected_games_missed
  
 
  
st.text(player_info['Best Pos_LM'])
st.text(player_info['Club_Burnley'])
st.text(pred_calc)
st.text(risk_calc(pred_calc))
st.text('This player is expected to miss ' expected_games_missed(pred_calc) ' games per season.)
st.text(player_importance[player_importance_select])
