import pandas as pd
import streamlit as st
from plotnine import *
st.title('Funders, Types, and Countries')

st.write('This page displays the relationship between funders and topics based on funder types and countries.')

topic = pd.read_csv('type.csv')
topic_name = topic.columns[:100]
country = pd.read_csv('country.csv')
country_name = country.drop_duplicates('Country')['Country'].tolist()
topic_name = st.selectbox(
    'Which topic would you like to explore?',
    topic_name)



p1 = ggplot(topic[topic['Publication Year']>=2007][topic['Publication Year']!=2021], aes('Publication Year', topic_name, color = 'Type')) + geom_smooth(se = False) + geom_point()

st.pyplot(ggplot.draw(p1))


st.write('Which countries (where the funders come from) would you like to explore?')
country_name1 = st.selectbox('Country 1', country_name, index = 200)

country_name2 = st.selectbox('Country 2', country_name, index = 38)

data = country[country['Publication Year']>=2007][country['Publication Year']!=2021][country['Country'].isin([country_name1, country_name2])]

p2 = ggplot(data, aes('Publication Year', topic_name, color = 'Country')) + geom_smooth(se = False) + geom_point()

st.pyplot(ggplot.draw(p2))