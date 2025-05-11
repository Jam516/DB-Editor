#--------------------------------------------------------#
# Imports
#--------------------------------------------------------#
import streamlit as st

#--------------------------------------------------------#
# Main Body
#--------------------------------------------------------#

st.set_page_config(
  page_title="Arbigrants Database Editor",
  page_icon="✨",
  layout="wide",
)

# Create the title at the tp of page
st.title('Arbigrants Database Editor')

st.markdown(
    """
    This app allows you to edit, add and delete rows from the Project tables of the Arbigrants database. Specifically,
    - PROJECT METADATA: This table contains desctiptive information on each project (description, category, social links .etc). One row per project.
    - PROJECT CONTRACTS: This table contains the contracts for all the projects. One row per contract.
    - PROJECT PROGRESS: This table contains the milestone progress for all the projects. One row per project.
    - DOWNLOAD LEADERBOARD: This tool allows you to download the leaderboard as a csv.
    
    **👈 Select a table from the sidebar**
"""
)