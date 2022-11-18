import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/PeterTXS09/streamlit_demo/main/USD_PEN%20Historical%20Data2.csv'
datos = pd.read_csv(url, sep=',')


st.title('Precio del dólar')
st.write('Analicemos el precio del dólar a lo largo del perido')
fig, ax = plt.subplots()
precio = datos['Price']
ax.hist(precio)
#st.pyplot(data=datos, x='Date', y='Price')
st.pyplot(precio)

st.title('Precio del dólar en el día - valor más alto y bajo')
st.write('Analicemos el precio del dólar a lo largo del perido establecido vs el valor más alto y más bajo')
st.line_chart(data=datos, x='Date', y=['Price', 'High', 'Low'])

st.title('Precio del dólar en volúmenes movidos')
st.write('Precio del dólar con respecto al día anterior')
st.line_chart(data=datos, x='Date', y='Change')
