import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
from nltk.corpus import stopwords
import nltk
import calendar

st.set_page_config(page_title="Exercicio 2", page_icon="📈", layout="wide")

nltk.download('stopwords')
stop_words = set(stopwords.words('portuguese'))

st.title('Ocorrências no Reclame aqui')


def load_data(file_name):
    df = pd.read_csv(file_name)
    df['TEMPO'] = pd.to_datetime(df['TEMPO'])
    df['UF'] = df['LOCAL'].apply(lambda x: x.split('-')[-1] if len(x.split('-')[-1]) != 2 else 'NF' )
    df['CIDADE'] = df['LOCAL'].apply(lambda x: x.split('-')[0].strip() if len(x.split('-')[-1]) != 2 else 'NF')


    col1, col2, col3 = st.columns(3)

    with col1:
        ano = st.selectbox('Ano', index=None, placeholder="Selecione um ano", options=df['ANO'].unique())

    with col2:
        estado  = st.selectbox('UF',index=None, placeholder="Selecione um estado", options=df['UF'].unique())

    with col3:
        status = st.multiselect('Status', placeholder="Selecione um status", options=df['STATUS'].unique())

    df_filtered = df

    if ano:
        df_filtered = df_filtered[df_filtered['ANO'] == ano]
    if estado:
        df_filtered = df_filtered[(df_filtered['UF']== estado)]
    if status:
        df_filtered = df_filtered[(df_filtered['STATUS'].isin(status))]


    df_grouped = df_filtered.groupby(['ANO', 'MES'], as_index=False)['CASOS'].count()
    df_status = df_filtered.groupby("STATUS", as_index=False)['CASOS'].count()


    st.markdown("<br>", unsafe_allow_html=True)


    col4, col5, col6 = st.columns(3)

    with col4:
        total_cases = df_grouped['CASOS'].sum()

        st.markdown("###### Total de ocorrências")
        box_content = f"""
        <div style="background-color: #262730; padding: 10px; border-radius: 5px;">
            <p style="font-size: 24px; font-weight: bold; margin: 0;">{total_cases}</p>
        </div>
        """

        st.markdown(box_content, unsafe_allow_html=True)

    with col5:
        if total_cases > 0:
            cases_by_cities = df_filtered.groupby(['CIDADE'])['CASOS'].sum()
            most_cases_citie = cases_by_cities.idxmax()
            cases_in_citie = cases_by_cities.loc[most_cases_citie]
            text = f'{most_cases_citie} - {cases_in_citie} ocorrências'
        else:
            text = 'Não se aplica'

        st.markdown("###### Cidade com mais")
        box_content = f"""
        <div style="background-color: #262730; padding: 10px; border-radius: 5px;">
            <p style="font-size: 24px; font-weight: bold; margin: 0;">{text}</p>
        </div>
        """

        st.markdown(box_content, unsafe_allow_html=True)

    with col6:
        if total_cases > 0:
            cases_by_day = df_filtered.groupby(['DIA_DA_SEMANA'])['CASOS'].sum()
            most_cases_day = cases_by_day.idxmax()
            cases_in_day = cases_by_day.loc[most_cases_day]
            day_name = calendar.day_name[most_cases_day - 1]
            text = f'{day_name} - {cases_in_day}'
        else:
            text = 'Não se aplica'

        st.markdown("###### Dia da semana com mais ocorrências")
        box_content = f"""
        <div style="background-color: #262730; padding: 10px; border-radius: 5px;">
            <p style="font-size: 24px; font-weight: bold; margin: 0;">{text}</p>
        </div>
        """

        st.markdown(box_content, unsafe_allow_html=True)



    col7, col8 = st.columns(2)

    with col7:
        bar = px.bar(df_grouped, x="MES", y="CASOS", color="ANO", 
                      title="Reclamações",
                      labels={
                            "CASOS": "Reclamações no período",
                            "ANO": "Ano",
                            "MES": "Mês"
                        })
    
        st.plotly_chart(bar, use_container_width=True)

    with col8:
        line = px.line(df_grouped, x="MES", y="CASOS", color="ANO", 
                      markers=True, 
                      title="Reclamações",
                      labels={
                            "CASOS": "Reclamações no período",
                            "ANO": "Ano",
                            "MES": "Mês"
                        })
        st.plotly_chart(line, use_container_width=True)


    col9, col10 = st.columns(2)
        
    with col9:
        tree = px.pie(df_status, values="CASOS" ,
                      names="STATUS",   
                      title="Status de solução de problemas",
                      labels={
                          "STATUS": "Status",
                          "CASOS": "Quantidade de ocorrências"
                      }, 
                      hole=0.6)
        
        st.plotly_chart(tree, use_container_width=True)

    with col10:
        # lollipop = px.scatter(df_filtered, x='STATUS', y='CASOS', title='Lollipop Chart', labels={'STATUS': 'Quantidade de ocorrências'})
        # st.plotly_chart(lollipop, use_container_width=True)
        heatmap = px.density_heatmap(data_frame=df_filtered, 
                                     x='ANO', 
                                     y='STATUS', 
                                     z='CASOS', 
                                     labels={
                                         'CASOS': 'Ocorrências', 
                                         'ANO': 'Ano', 
                                         'STATUS': 'Status'
                                         }, 
                                     title='Heatmap')
        st.plotly_chart(heatmap, use_container_width=True)
        # heatmap = px.imshow(df_filtered, labels=dict(x="Status", y="Quantidade de ocorrências"), x=df_filtered['STATUS'].values, y=df_filtered['CASOS'])
        # heatmap.update_layout(title='Heatmap Example', width=600, height=400)
        # st.image(image=heatmap, use_column_width=True)



    if total_cases > 0:
        wc_text = ' '.join(df_filtered['DESCRICAO'])
        wc_filtered = ' '.join([word for word in wc_text.split() if word.lower() not in stop_words])

        wordcloud = WordCloud(width=800, height=400, background_color='black').generate(wc_filtered)
        st.markdown("###### Nuvem de palavras")
        st.image(image=wordcloud.to_array(), use_column_width=True)
    



tab1, tab2, tab3 = st.tabs(["Ibyte","Hapvida","Nagem"])

with tab1:
    load_data('./data/RECLAMEAQUI_IBYTE.csv')
with tab2:
    load_data('./data/RECLAMEAQUI_HAPVIDA.csv')
with tab3:
    load_data('./data/RECLAMEAQUI_NAGEM.csv')