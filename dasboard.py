import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("./data/RECLAMEAQUI_NAGEM.csv", encoding='latin-1')

profile = ProfileReport(df, title='Reclame aqui Nagem')

profile.to_file('RECLAMEAQUI_NAGEM.html')