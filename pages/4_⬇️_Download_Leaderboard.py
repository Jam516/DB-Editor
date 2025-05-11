import pandas as pd
import json
import streamlit as st
import time

st.set_page_config(layout="wide", page_title="Leaderboard", page_icon="🧮")

conn = st.connection("snowflake")

st.title("Leaderboard 🧮")

session = conn.session()

df = session.table("ARBIGRANTS_ALL_MONTH_LEADERBOARD").to_pandas()
df = df.sort_values(by="ETH_FEES", ascending=False)

csv = df.to_csv(index=False)
st.download_button(
    label="Download Month Leaderboard",
    data=csv,
    file_name="month_leaderboard.csv",
    mime="text/csv",
    icon=":material/download:",
)