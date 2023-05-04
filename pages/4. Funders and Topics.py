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
st.dataframe(search.drop(['paper_id', 'Name', 'Country', 'Type'], 1))


#ff = pd.DataFrame(search.drop(['paper_id', 'Name', 'Country', 'Type'], 1).mean())
ff.columns = ['Proportion']
ff = ff.sort_values('Proportion', ascending = False)
ff['Topic'] = ff.index
ff.index = range(len(ff))

st.write(len(search), 'papers were funded by', option)
st.write('This table displays the proportions of topics funded by', option, 'from large to small.')
st.dataframe(ff, height = 800, width = 700)
