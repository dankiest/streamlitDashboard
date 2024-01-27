import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import ydata_profiling
from ydata_profiling import ProfileReport

st.set_page_config(page_title="Profillings", page_icon="📈", layout="wide")

st.title('Profillings dos dados utilizados no projeto')

tab1, tab2 = st.tabs(["Exercicio 1", "Exercicio 2"])

with tab1:
    with open('./profilling/spotify_songs.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    st.components.v1.html(html_content, height=1600, scrolling=True)

with tab2:
    tab3, tab4, tab5 = st.tabs(["Ibyte","Hapvida","Nagem"])

    with tab3:
        with open('./profilling/RECLAMEAQUI_IBYTE.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=1600, scrolling=True)

    with tab4:
        with open('./profilling/RECLAMEAQUI_HAPVIDA.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=1600, scrolling=True)

    with tab5:
        with open('./profilling/RECLAMEAQUI_NAGEM.html', 'r', encoding='utf-8') as file:
            html_content = file.read()
        st.components.v1.html(html_content, height=1600, scrolling=True)