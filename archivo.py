import pandas as pd
import streamlit as st
import numpy as np

st.title('Precio del dólar')
url = 'https://raw.githubusercontent.com/PeterTXS09/streamlit_demo/main/USD_PEN%20Historical%20Data2.csv'
datos = pd.read_csv(url, sep=',')

st.line_chart(data=datos, x='Date', y='Price')

st.line_chart(data=datos, x='Date', y=['Price', 'High', 'Low'])

