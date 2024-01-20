import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("RECLAMEAQUI_NAGEM.csv", encoding='latin-1')

profile = ProfileReport(df, title='Most streamed Spotify Songs of 2023')

profile.to_file('RECLAMEAQUI_NAGEM.html')