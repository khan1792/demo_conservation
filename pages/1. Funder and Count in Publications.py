import pandas as pd
import streamlit as st

st.title('Funder Names and Their Counts in Publications')
st.write('This table displays a list of funder names and how many scholarly papers they supported.')

occur = pd.read_csv('funder_occur.csv')
occur['established'] = occur['established'].apply(lambda x: str(int(x)))

st.write('Click any column to sort')
st.write("Double click a funder name in a table cell if it's too lengthy to display")
st.dataframe(occur, height = 800, width = 1000)
