import streamlit as st
import pandas as pd
import numpy as np
st.title('Datos aleatorios')
n = st.slider("n", 5,100, step=1)
df = pd.read_excel('wine.xlsx')
chart_data = pd.DataFrame(np.random.randn(n),columns=['data'])
st.line_chart(df)
