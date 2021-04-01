import streamlit as st
import pandas as pd
from pickle import load
from sklearn.linear_model import LogisticRegression

def process(df):
    st.header("educational-num ( Number of Education Year )")
    educational_num = st.slider("",0,10,1)
    
    st.header("capital-gain")
    capital_gain = st.number_input("")
    
    st.header('Education')
    education = st.selectbox("",['education_1st-4th','education_5th-6th','None of them'])
    if(education == 'education_1st-4th'):
        education_1st_4th  = 1
        education_5th_6th=0
        None_of_them = 0
    elif(education == 'education_5th-6th'):
        education_5th_6th  = 1
        education_1th_4th=0
        None_of_them = 0
    elif(education == 'None of them'):
        None_of_them  = 1
        education_1th_4th=0
        education_5th_6th = 0

    st.header("Marital-Status")
    marital_status = st.selectbox("",['marital-status_Married-AF-spouse','marital-status_Married-civ-spouse', 'marital-status_Never-married','None of them'])
    if(marital_status == 'marital-status_Married-AF-spouse'):
        marital_status_Married_AF_spouse  = 1
        marital_status_Married_civ_spouse=0
        marital_status_Never_married=0
        None_of_them = 0
    if(marital_status == 'marital-status_Married-civ-spouse'):
        marital_status_Married_civ_spouse  = 1
        marital_status_Married_AF_spouse=0
        marital_status_Never_married=0
        None_of_them = 0
    if(marital_status == 'marital-status_Never-married'):
        marital_status_Never_married  = 1
        marital_status_Married_AF_spouse=0
        marital_status_Married_civ_spouse=0
        None_of_them = 0
    if(marital_status == 'None of them'):
        None_of_them  = 1
        marital_status_Married_AF_spouse=0
        marital_status_Married_civ_spouse=0
        marital_status_Never_married = 0

    st.header('Occupation')
    occupation = st.selectbox("",['occupation_Farming-fishing', 'occupation_Handlers-cleaners', 'occupation_Other-service', 'occupation_Priv-house-serv','None of them'])
    if(occupation == 'occupation_Farming-fishing'):
        occupation_Farming_fishing  = 1
        occupation_Handlers_cleaners=0
        occupation_Other_service=0
        occupation_Priv_house_serv=0
        None_of_them = 0
    if(occupation == 'occupation_Handlers-cleaners'):
        occupation_Handlers_cleaners  = 1
        occupation_Farming_fishing=0
        occupation_Other_service=0
        occupation_Priv_house_serv=0
        None_of_them = 0
    if(eoccupation == 'occupation_Other-service'):
        occupation_Other_service  = 1
        occupation_Farming_fishing=0
        occupation_Handlers_cleaners=0
        occupation_Priv_house_serv=0
        None_of_them = 0
    if(occupation == 'occupation_Priv-house-serv'):
        occupation_Priv_house_serv  = 1
        occupation_Farming_fishing=0
        occupation_Handlers_cleaners=0
        occupation_Other_service=0
        None_of_them = 0
    if(occupation== 'None of them'):
        None_of_them  = 1
        occupation_Farming_fishing=0
        occupation_Handlers_cleaners=0
        occupation_Other_service=0
        occupation_Priv_house_serv = 0

    st.header('Relationship')
    relationship = st.selectbox("",['relationship_Other-relative', 'relationship_Own-child','relationship_Wife','None of them'])
    if(relationship == 'relationship_Other-relative'):
        relationship_Other_relative  = 1
        relationship_Own_child=0
        relationship_Wife=0
        None_of_them = 0
    if(relationship == 'relationship_Own-child'):
        relationship_Own_child  = 1
        relationship_Other_relative=0
        relationship_Wife=0
        None_of_them = 0
    if(relationship == 'relationship_Wife'):
        relationship_Wife  = 1
        relationship_Other_relative=0
        relationship_Own_child=0
        None_of_them = 0
    if(relationship == 'None of them'):
        None_of_them  = 1
        relationship_Other_relative=0
        relationship_Own_child=0
        relationship_Wife = 0

    st.header('Gender')
    gender = st.selectbox('',['Male','Female'])
    if(gender =='Male'):
        gender_value = 1
    if(gender == 'Female'):
        gender_value = 0
    
    st.header('Native-Country')
    native = st.selectbox('',['Columbia', 'Dominican-Republic', 'El-Salvador', 'Laos', 'Mexico', 'Peru', 'Scotland', 'South','Trinadad&Tobago', 'Vietnam','Other'])
    if(native=='Columbia'):
        Columbia = 1
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Dominican-Republic'):
        Dominican_Republic = 1
        Columbia=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='El-Salvador'): 
        El_Salvador = 1
        Columbia=0
        Dominican_Republic=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Laos'):
        Laos = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Mexico'):
        Mexico = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Peru'):
        Peru = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Scotland'):
        Scotland = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        South=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='South'):
        South = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        Trinadad_Tobago=0
        Vietnam=0
        Other = 0
    if(native=='Trinadad&Tobago'):
        Trinadad_Tobago = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Vietnam=0
        Other = 0
    if(native=='Vietnam'):
        Vietnam = 1
        Columbia =0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Other = 0
    if(native=='Other'):
        Other = 1
        Columbia=0
        Dominican_Republic=0
        El_Salvador=0
        Laos=0
        Mexico=0
        Peru=0
        Scotland=0
        South=0
        Trinadad_Tobago=0
        Vietnam = 0

def main():
    st.title('Adult Census Income Predictor')

    classifier_loc = "pickle/logit_model.pkl"

    process(classifier_loc)
    
    data = [educational_num,capital_gain,education_1th_4th,education_5th_6th,
    marital_status_Married_AF_spouse,marital_status_Married_civ_spouse,marital_status_Never_married,
    occupation_Farming_fishing,occupation_Handlers_cleaners,occupation_Other_service,occupation_Priv_house_serv,
    relationship_Other_relative,relationship_Own_child,relationship_Wife,
    gender_value,Columbia,Dominican_Republic,El_Salvador,Laos,Mexico,Peru,Scotland,South,Trinadad_Tobago,Vietnam]

    classifier = load(open('pickle/logit_model.pkl', 'rb'))
    prediction = classifier.predict(data)

    if(prediction):
        st.subheader("Prediction:")
        if(prediction == 0):
            st.image("Your Income is greater that 50K", use_column_width = True)

        else:
            st.image("Your income is less than 50K", use_column_width = True)

if(__name__ == '__main__'):
    main()