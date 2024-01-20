import streamlit as st
import pandas as pd
import numpy as np

st.title('é o laion')
st.write('ñ tem jeito')


df = pd.read_csv("RECLAMEAQUI_HAPVIDA.csv", encoding='latin-1')

df['TEMPO']=pd.to_datetime(df['TEMPO'])

df['LOCAL'].iloc[0].split(' - ')[1].strip()

estado_lista=[]
for i in range(len(df)):
    estado_lista.append(df['LOCAL'].iloc[i].split('-',2)[1].strip())


df['ESTADO']=estado_lista

hist_values = np.histogram(df['TEMPO'].dt.year, bins=24, range=(0,24))[0]

st.bar_chart(hist_values)

