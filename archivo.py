import pandas as pd
import streamlit as st
import numpy as np

cols = ['Date','Price','Open','High','Low','Vol.','Change %']
url = 'https://raw.githubusercontent.com/PeterTXS09/streamlit_demo/main/USD_PEN%20Historical%20Data2.csv'
datos = pd.read_csv(url, header=None, sep=',', names=cols, error_bad_lines=False)
datos.Price = datos.Price.fillna(int(0))
datos.Price = datos.Price.astype(float)

st.line_chart(data=datos, x='Date', y='Price')
