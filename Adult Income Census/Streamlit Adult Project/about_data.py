import streamlit as st
import pandas as pd

dataset_loc = 'data/adult.csv'

@st.cache

def load_data(dataset_loc):
    df = pd.read_csv(dataset_loc, sep="\t",names = ['label','message'], error_bad_lines=False)
    return df

def about_dataset(df):
    st.header('Adult Dataset')
    st.info('This data was extracted from the 1994 Census bureau database by Ronny Kohavi and Barry Becker'
    '(Data Mining and Visualization, Silicon Graphics).'
    '\n \n *  In this Dataset we have 48842 observation and 15 attributes including target attribute(income).'
    '\n \n * Where it have Categorical and numeric variabels in attribute.'
    '\n \n * Attributes with numeric values are \'age\', \'fnlwgt\', \'educational-num\', \'capital-gain\', \'capital-loss\' and \'hours-per-week \'.'
    '\n \n * Attributes with categorical values are \'workclass\', \'education\', \'marital-status\', \'occupation\', \'relationship\', \'race\',\'gender\' and \'income\'.')

    st.header('Attribute Information')
    st.info('\n \n * age: continuous.'
    '\n \n * workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.'
    '\n \n * fnlwgt: continuous.'
    '\n \n * education: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.'
    '\n \n * education-num: continuous.'
    '\n \n * marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.'
    '\n \n * occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.'
    '\n \n * relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.'
    '\n \n * race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.'
    '\n \n * sex: Female, Male.'
    '\n \n * capital-gain: continuous.'
    '\n \n * capital-loss: continuous.'
    '\n \n * hours-per-week: continuous.'
    '\n \n * native-country: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.'
    '\n \n * income: >50K, <=50K')

 








def main():
    df = load_data(dataset_loc)

    about_dataset(df)    

if(__name__ == '__main__'):
    main()