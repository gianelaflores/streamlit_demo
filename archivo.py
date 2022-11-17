import streamlit as st
from st_aggrid import AgGrid
import pandas as pd
st.title('Datos aleatorios')

df = pd.read_csv('https://raw.githubusercontent.com/fivethirtyeight/data/master/airline-safety/airline-safety.csv')
AgGrid(df)
