import pandas as pd
import streamlit as st
import numpy as np

@st.experimental_memo
def download_data():
    cols = ['Date','Price','Open','High','Low','Vol.','Change %']
    url = 'https://github.com/PeterTXS09/streamlit_demo/blob/main/USD_PEN%20Historical%20Data2.csv'
    df = pd.read_csv(url, header=None, sep=',', names=cols)
    return df

datos = download_data()
st.bar_chart(datos['Price'])
