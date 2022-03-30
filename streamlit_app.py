import streamlit as st
import numpy as np
import pandas as pd
import datetime


player_info = {"Age": 20,
              "Work_Rate": 15,
              "% Games Played When Fit": 0.8,
              "Club_Arsenal": 0,
              "Club_Aston Villa": 0,
              "Club_Brighton": 0,
              "Club_Burnley": 0,
              "Club_Chelsea": 0,
              "Club_Crystal Palace": 0,
              "Club_Everton": 1,
              "Club_Fulham": 0,
              "Club_Leeds United": 0,
              "Club_Leicester City": 0,
              "Club_Liverpool FC": 0,
              "Club_Manchester City": 0,
              "Club_Manchester United": 0,
              "Club_Newcastle United": 0,
              "Club_Sheffield United": 0,
              "Club_Southampton": 0,
              "Club_Tottenham Hotspur": 0,
              "Club_West Bromwich Albion": 0,
              "Club_West Ham United": 0,
              "Club_Wolverhampton Wanderers": 0,
              "Best Pos_CM": 1,
              "Best Pos_GK": 0,
              "Best Pos_LD": 0,
              "Best Pos_LM": 0,
              "Best Pos_RD": 0,
              "Best Pos_RM": 0,
              "Best Pos_ST": 0,
              "Best Pos_CD": 0
              }

st.text(player_info('Age')
