import pandas as pd
import streamlit as st

st.title('Topics Occurred in Publications')

st.write('This table displays 100 research topics uncovered by an unsupervised machine learning technique (structural topic modeling) based on abstracts and titles of all conservation science papers')

name = pd.read_csv('topic_name.csv')
st.write('Click column to sort')
st.dataframe(name, height = 650, width = 800)