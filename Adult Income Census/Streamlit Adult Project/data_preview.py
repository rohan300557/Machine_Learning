import streamlit as st
import pandas as pd
import seaborn as se
import matplotlib.pyplot as plt
import plotly.express as px

dataset_loc = 'data/adult.csv'

@st.cache

def load_data(dataset_loc):
    missing_val = '?'
    df = pd.read_csv(dataset_loc,na_values = missing_val)
    return df

def data_preveiw(df):
    st.header("Data Preview")
    if(st.checkbox("Top/Bottom rows of Dataset")):
        preview = st.radio("Choose one", ("Top", "Bottom"))
        if(preview == "Top"):
            st.write(df.head())
        if(preview == "Bottom"):
            st.write(df.tail())

    if(st.checkbox("Complete Dataset")):
        st.dataframe(df)
        st.info('\n * In Adult Census Income Dataset the  missing values are present in the form of "?" in "workclass", "occupation",'
         ' and "native-country" columns. So we have replaced it with NaN (not a null) for identifying them as missing value for further analysis.'
         '\n \n * We also have removed unnecessary column from the dataset i.e. \'fnlwgt\'.')
        
    if(st.checkbox("Display the shape")):
        st.write(df.shape)
        dim = st.radio("Rows/Columns?", ("Rows", "Columns"))
        if(dim == "Rows"):
            st.write("Number of Rows", df.shape[0])
        if(dim == "Columns"):
            st.write("Number of Columns", df.shape[1])

    if(st.checkbox('Identifying Missing Values in Columns')):
        st.write(df.isnull().sum())
        st.info('In this Dataset the respected columns \'workclass\' have 2799 missing' 
        'values followed by \'occupation\' having 2809 missing values and \'native-country\' having 857 missing values.')
    
    if(st.checkbox('Descriptive Statistics')):
        preview = st.radio("Select one", ("Non Categorical", "Categorical"))
        
        if(preview == "Non Categorical"):
            st.write(df.describe(include='number'))
            st.info('Following Observation :'
                    '\n \t \n Age :'
                    '\n \n * This attribute has Age of an individual.'
                    '\n \n * The mean value is 38. Age is having the standerd deviation 13.71.'
                    '\n \n * The value of Age attribute varies from 17 to 90.'
                    '\n \n **Educational-num :**'
                    '\n \n * This attribute has Individual\'s year of receiving education.'
                    '\n \n * The mean value is 10 and median is 10.'
                    '\n \n Capital-gain :'
                    '\n \n * For capital-gain, the mean is 1101.43 and median is 0, which indicates that the distribution is highly right skewed.'
                    '\n \n * In the attribute capital-gain shows that either a person has no gain/profit or has gain of very large amount.'
                    '\n \n Capital-loss :'
                    '\n \n * This attribute is similar to the capital-gain i.e. either a person has no loss or has loss with very large amount.'
                    '\n \n * The Mean is 88 but median is 0.'
                    '\n \n Hours-per-week :'
                    '\n \n * This attribute means number of working hours spend by an individual in a week.'
                    '\n \n * This data the hours-per-week atrribute varies within the range of 1 to 99.')
        if(preview == "Categorical"):
            st.write(df.describe(include=['O']))
            st.info('Following Observation :'
                    '\n \n **-Age**'
                    '\n \n * In this attributes shows the Individual work category.'
                    '\n \n * The top category in workclass is \'Private\' and the Frequency of \'Private\' is 33307.'
                    '\n \n * There are 7 unique categories present in the workclass attribute.'
                    '\n \n **-Education**'
                    '\n \n * The attribute \'education\' shows the Individual\'s highest education degree.'
                    '\n \n * The top category in education is \'HS-grad\' and the Frequency of \'HS-grad\' is 14783.'
                    '\n \n * There are 16 unique categories present in the workclass attribute.'
                    '\n \n**-Marital-status**'
                    '\n \n * The attribute \'marital-status\' shows the Individual marital status.'
                    '\n \n * The top category in marital-status is \'Married-civ-spouse\' and the Frequency of \'Married-civ-spouse\' is 21055.'
                    '\n \n * There are 7 unique categories present in the marital-status attribute.'
                    '\n \n**-Occupation**'
                    '\n \n * The attribute \'occupation\' shows the Individual\'s occupation.'
                    '\n \n * The top category in occupation is \'Craft-repair\' and the Frequency of \'Craft-repair\' is 6020.'
                    '\n \n * There are 17 unique categories present in the occupation attribute.'
                    '\n \n**-Relationship**'
                    '\n \n * The attribute \'relationship\' shows the Individual\'s relation in a family.'
                    '\n \n * The top category in relationship is \'Husband\' and the Frequency of \'Husband\' is 18666.'
                    '\n \n * There are 6 unique categories present in the relationship attribute.'
                    '\n \n**-Race**'
                    '\n \n * The attribute \'race\' shows the Race of Individual.'
                    '\n \n * The top category in race is \'White\' and the Frequency of \'White\' is 38903.'
                    '\n \n * There are 5 unique categories present in the race attribute.'
                    '\n \n**-Gender**'
                    '\n \n * The top category in gender is \'Male\' and the Frequency of \'Male\' is 30527.'
                    '\n \n * There are 2 unique categories present in the gender attribute.'
                    '\n \n**-Native-country**'
                    '\n \n * The attribute \'native-country\' shows the Individual\'s native country.'
                    '\n \n * The top category in native-country is \'United-States\' and the Frequency of \'United-States\' is 41292.'
                    '\n \n * There are 41 unique categories present in the native-country attribute.')





def main():
    df = load_data(dataset_loc)

    data_preveiw(df)

if(__name__ == '__main__'):
    main()