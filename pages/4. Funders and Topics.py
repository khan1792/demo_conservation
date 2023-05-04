import pandas as pd
import streamlit as st

st.title('Relationship between Funders and Topics')

final = pd.read_csv('final_data.txt.gz')
occur = pd.read_csv('funder_occur.csv')

name = occur['funder']


option = st.selectbox(
    'Which funder would you like to explore?',
    name)

search = final[final['Name'] == option]
