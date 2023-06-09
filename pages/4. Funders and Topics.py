import pandas as pd
import streamlit as st

st.title('Relationship between Funders and Topics')

final = pd.read_csv('final_data.txt.gz')
occur = pd.read_csv('funder_occur.csv')

name = occur['funder']


option = st.selectbox(
    'Which funder would you like to explore? You can also type a funder name to search.',
    name)

search = final[final['Name'] == option]
ff = pd.DataFrame(search.mean(numeric_only = True))[1:]
ff.columns = ['Proportion']
ff = ff.sort_values('Proportion', ascending = False)
ff['Topic'] = ff.index
ff.index = range(len(ff))

st.write(len(search), 'papers were funded by', option, '- an organization in', search['Country'].tolist()[0])
st.write('This table displays the proportions of topics funded by', option, 'from large to small.')
st.dataframe(ff, height = 800, width = 700)
