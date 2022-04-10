import streamlit as st
from utils import chunk_array, indexing_api

st.title('GSC Indexing API')

with st.form(key="url_form"):
    urls = st.text_area('Copy the urls', height=400)
    submit_btn = st.form_submit_button(label = "Submit")

if submit_btn:
    clean_urls = list(set(urls.split('')))
    chunk_urls = chunk_array(clean_urls, 75)

    try:
        for group in chunk_urls:
            request = indexing_api(group)

        st.success('Se ha solicitado la indexacion con exito')
    except Exception as e:
        st.error('Ha habido un error')
