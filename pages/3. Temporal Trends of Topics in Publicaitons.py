import pandas as pd
import streamlit as st
from plotnine import *
st.title('Topic Trends in Publications')

st.write('This figure displays the temporal trends of topics in previous conservaton publications. Since the Web of Science started recording funding informaiton mainly in and after 2007, we ploted topic trends for funded projects in and after 2007 (blue) and all projects seperately.')

topic = pd.read_csv('topic_trend.csv')
topic_name = topic.columns[:100]

topic_name = st.selectbox(
    'Which topic would you like to explore?',
    topic_name)


p1 = ggplot(topic[topic['Publication Year']!=2021], aes('Publication Year', topic_name, color = 'Type')) + geom_smooth(se = False)  + geom_point()




st.pyplot(ggplot.draw(p1))