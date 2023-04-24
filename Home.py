import streamlit as st

st.title('Funding Allocation in Scholarly Publications')

st.write('This demo can help you explore funding allocation in previous academic studies. It is based on more than 120k publication records in the domain of conservation science on the Web of Science (WOS). Since WOS started recording funding information mainly in and after 2007, the results here mainly reflect the funding allocation in conservation science studies since 2007. More interactive features and more accurate results will be added over time.')
st.write('It is worth noting that we used machine learning techinqiues to disambuate funder information because it was messay in the raw data, as well as to identify research topics of every paper and to predict funder type. The results is not 100% accurate.')