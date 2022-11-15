import streamlit as st
import pandas as pd
import numpy as np
import urllib.request
st.title('Datos Demo')

@st.experimental_memo
def download_data():
  url = 'https://files.minsa.gob.pe/s/eRqxR35ZCxrzNgr/download'
  filename = 'data.csv'
  urllib.request.urlretrieve(url, filename)
