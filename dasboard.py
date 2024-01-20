import pandas as pd
from ydata_profiling import ProfileReport


df = pd.read_csv("278k_labelled_uri.csv", na_values=['='])

profile = ProfileReport(df, title='Emotion Labeled Spotify Songs')

profile.to_file('278k_labelled_uri.csv.html')