import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import ydata_profiling
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report


st.set_page_config(page_title="Exercicio 1", page_icon="📈", layout="wide")


st.title('30000 Músicas do Spotify')

df = pd.read_csv('./data/spotify_songs.csv')
# st.dataframe(df)


def load_data():
    target = [
        { 'key': 'danceability', 'value': 'Dançabilidade' },
        { 'key': 'energy', 'value': 'Energia' },
        { 'key': 'loudness', 'value': 'Intensidade' },
        { 'key': 'speechiness', 'value': 'Fala' },
        { 'key': 'acousticness', 'value': 'Acusticidade' },
        { 'key': 'instrumentalness', 'value': 'Instrumentalidade' },
        { 'key': 'liveness', 'value': 'Vivacidade' },
        { 'key': 'valence', 'value': 'Valência' }
    ]

    col1, col2 = st.columns(2)

    with col1: 
        selected_target = st.selectbox('Target', options=[item['value'] for item in target], index=0)

    with col2:
        genres = st.multiselect('Gênero', placeholder="Selecione um gênero", options=df['playlist_genre'].unique())


    df_filtered = df

    if selected_target:
        selected_target_key = next(item['key'] for item in target if item['value'] == selected_target)

    if genres:
        df_filtered = df_filtered[df_filtered['playlist_genre'].isin(genres)]


    if selected_target:
        hist_title = f'Distribuição de {selected_target}'
        bar_title = f'{selected_target} Por gênero'
        box_plot_title = f'Distribuição de {selected_target}'


    col3, col4 = st.columns(2)

    with col3:
        scatter_plot = px.scatter(df_filtered, x=selected_target_key, y="playlist_genre", title=bar_title)
        st.plotly_chart(scatter_plot, use_container_width=True)
        

    with col4:
        hist = px.histogram(df_filtered, x=selected_target_key, title=hist_title)
        st.plotly_chart(hist, use_container_width=True)
        

    col5, col6 = st.columns(2)

    with col5:
        bar = px.bar(df_filtered, x="playlist_genre", y=selected_target_key, title=bar_title)
        st.plotly_chart(bar, use_container_width=True)

    with col6:
        box_plot = px.box(df_filtered, x="playlist_genre", y=selected_target_key, title=box_plot_title)
        st.plotly_chart(box_plot, use_container_width=True)



tab1, tab2 = st.tabs(["Dashboard", "Perguntas"])

with tab1:
    load_data()
with tab2:

    st.markdown("""

        ##### Qual a origem do meu dado?
         - Esse dado foi retidado do [kaggle](https://www.kaggle.com/datasets/joebeachcapital/30000-spotify-songs?select=spotify_songs.csv)
         - Nesse dado constam 30000 músicas retiradas da api do Spotify
                
        ##### Qual é o problema?
         - Esse dado demonstra várias métricas referentes a essas músicas 
         - Esse projeto toma por objetivo quantificar essas várias métricas com base em gêneros de música

        ##### Qual é a variável ALVO (target)?
         - Esse dado pode ter vários targets (Dançabilidade, Energia, Intensidade, Fala, Acusticidade, Instrumentalidade, Vivacidade, Valência)
                
        ##### Porque eu me importo?
         - Gosto de músicas e posso utilizar esses dados para encontrar músicas que não conheço com base em targets definidos.
                
        ##### Quais os ganhos possíveis no entendimento do meu dado?
         - Possibilidade de encontrar novas músicas com base em métricas
         - Possibilidade de entender quais tipos de métricas estão em mais playlists, consequentemente quais músicas são mais escutadas
    """)
