import pandas as pd
import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Spotify songs"
)


@st.cache_data
def load_data():
    df = pd.read_csv("csv/spotify.csv")
    return df


st.session_state["df_spotify"] = load_data()


df = load_data()
df.set_index('Track', inplace=True)

artists = df["Artist"].value_counts().index
artist = st.sidebar.selectbox('Artist', artists)
df_filtered = df[df["Artist"] == artist]

albuns = df_filtered["Album"].value_counts().index
album = st.sidebar.selectbox('Album', albuns)

df_filtered2 = df[df["Album"] == album]

col1, col2 = st.columns([0.7, 0.3])

col1.bar_chart(df_filtered2["Stream"])
col2.line_chart(df_filtered2["Danceability"])

st.write(artist)
