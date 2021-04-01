import streamlit as st
import about_data as ad
import data_preview as dp
import eda as ed
import data_prediction as d_p
def sidebar():
    
    st.sidebar.title("About")
    st.sidebar.info(
        "This an open source project. " 
        "This app is maintained by **Rohan Gupta**. " 
        "Go check out my [Github account](https://github.com/rohan300557) :grinning: ")


st.title('Adult Census Income')

if(st.sidebar.checkbox('About Dataset')):
    st.image("data/adult_income.jpg", use_column_width = True)
    ad.main()
if(st.sidebar.checkbox('Data Preview')):
    st.image("data/adult_income.jpg", use_column_width = True)
    dp.main()
if(st.sidebar.checkbox('EDA')):
    st.image("data/adult_eda.jpg", use_column_width = True)
    ed.main()
if(st.sidebar.checkbox('Income Predictor')):
    st.image("data/adult_income.jpg", use_column_width = True)
    d_p.main()
else:
    st.image("data/adult_income.jpg", use_column_width = True)
    sidebar()
