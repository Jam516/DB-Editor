import pandas as pd
import json
import streamlit as st
import time

st.set_page_config(layout="centered", page_title="Data Editor", page_icon="🧮")

conn = st.connection("snowflake")

st.title("Snowflake Table Editor ❄️")
st.caption("This is a demo of the `st.experimental_data_editor`.")

session = conn.session()

df = session.table("ARBIGRANTS_LABELS_PROJECT_METADATA").to_pandas()

with st.form("data_editor_form"):
    st.caption("Edit the dataframe below")
    edited_df = st.data_editor(df, num_rows="dynamic")
    submit_button = st.form_submit_button("Submit")

if submit_button:
    try:
        #Note the quote_identifiers argument for case insensitivity
        session.write_pandas(edited_df, "ARBIGRANTS_LABELS_PROJECT_METADATA", overwrite=True, quote_identifiers=False)
        st.success("Table updated")
        time.sleep(5)
    except:
        st.warning("Error updating table")
    #display success message for 5 seconds and update the table to reflect what is in Snowflake
    st.rerun()