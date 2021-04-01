import streamlit as st
import pandas as pd
import seaborn as se
import matplotlib.pyplot as plt
import plotly.express as px

dataset_loc = 'data/adult.csv'

@st.cache

def sidebar(df):
    st.sidebar.title("About")
    st.sidebar.info(
        "This an open source project. " 
        "This app is maintained by **Rohan Gupta**. " 
        "Go check out my [Github account](https://github.com/rohan300557) :grinning: ")

def load_data(dataset_loc):
    missing_val = '?'
    df = pd.read_csv(dataset_loc,na_values = missing_val)
    df.dropna(inplace=True)
    df.drop('fnlwgt',inplace=True,axis=1)
    return df

def countplot(df):
    st.title('-Countplot')
    sel = st.selectbox('Select one',['--Select One--', 'workclass','education','marital-status'
    ,'occupation','relationship','race','gender','native-country'])
    
    if(sel == 'workclass'):
        plt.figure(figsize=(10,5))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'education'):
        plt.figure(figsize=(20,10))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'marital-status'):
        plt.figure(figsize=(15,8))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'occupation'):
        plt.figure(figsize=(25,8))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'relationship'):
        plt.figure(figsize=(10,5))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'race'):
        plt.figure(figsize=(8,5))
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'gender'):
        st.write(se.countplot(sel,palette="Set2", data=df))
        st.pyplot()
    if(sel == 'native-country'):
        plt.figure(figsize=(10,5))
        plt.ylabel('counts')
        plt.xlabel('native-country')
        st.write(se.barplot(df['native-country'].value_counts().index[:5] , df['native-country'].value_counts().values[:5]))
        st.pyplot()

def piechart(df):
    st.title('-Piechart')
    sel = st.selectbox('Select one',['-- Select One --','workclass','gender','race','income'])
    if(sel == '-- Select One --'):
        pass
    else:
        st.write(plt.pie(df[sel].value_counts(),autopct='%.2f%%', shadow=True,labels=df[sel].unique()))
        st.pyplot()

def histogram(df):
    st.title('-Histogram')
    sel = st.selectbox('Select one',['-- Select One --','age','educational-num','capital-gain','capital-loss','hours-per-week'])
    if(sel == '-- Select One --'):
        pass
    else:
        plt.ylabel('Frequency')
        plt.xlabel(sel)
        st.write(se.distplot(df[sel], rug=True))
        st.pyplot()

def boxplot(df):
    st.title('-Boxplot')
    sel = st.selectbox('Select one',['-- Select One --','age','educational-num','capital-gain','capital-loss','hours-per-week'])
    if(sel == '-- Select One --'):
        pass
    else:
        st.write(se.boxplot(df[sel]))
        st.pyplot()

def probabilty(df):
    st.title('-PDF (Probability Distribution Function)')
    sel = st.selectbox('Select one',['-- Select One --','age','educational-num','capital-gain','capital-loss','hours-per-week'])
    if(sel == '-- Select One --'):
        pass
    else:
        plt.ylabel('Frequency')
        plt.xlabel(sel)
        st.write(se.distplot(df[sel],hist = False,kde=True))
        st.pyplot()



def scatter_plot(df):
    st.write(se.scatterplot(x = df['capital-gain'], y = df['capital-loss']))
    st.pyplot()

def hexbin_plot(df):
    sel = st.sidebar.selectbox('Between',['-- Select One --','Age and Hours-per-week','Capital-gain and Capital-loss'])
    if(sel == '-- Select One --'):
        st.info('Select any one........')
        pass
    if(sel == 'Age and Hours-per-week'):
        st.write(se.jointplot(x='age', y='hours-per-week',kind= 'hex', data=df, color='r'))
        st.pyplot()
    
    if(sel == 'Capital-gain and Capital-loss'):
        st.write(se.jointplot(x='capital-gain', y='capital-loss', data=df, kind='hex', color='g'))
        st.pyplot()
    
def pair_plot(df):
    st.write(se.pairplot(df,hue='income',palette="husl",markers=["o", "s"]))
    st.pyplot()
def box_plot(df):
    sel = st.selectbox('Between Income and..',['-- Select One --','age','educational-num','hours-per-week','capital-gain','capital-loss'])
    sel1 = st.selectbox('With hue (Optional)',['None','gender','income'])
    button = st.button('Create it')
    if(button == 'Create it'):
        if(sel1=='None'):
            if(sel == '-- Select One --'):
                st.info('Select any one........')
                pass
            else:
                st.write(se.boxplot(x="income", y=sel, data=df))
                st.pyplot()
        else:
            st.write(se.boxplot(x="income", y="age",hue=sel1,data=df))
            st.pyplot()

def heat_map(df):
    t1=df.corr()
    st.header('Heatmap')
    st.write(se.heatmap(t1,linewidths=.5,annot=True))
    st.pyplot()





def select_box(df):
    if(st.sidebar.checkbox('Univariate Analysis')):
        sel1 = st.sidebar.selectbox('Select Column type',['--Select One--','Non-Categorical','Categorical'])
        if(sel1 == 'Non-Categorical'):
            sel = st.sidebar.selectbox('Univariate Analysis (For Non Categorical variables',['--Select One--','Histogram','Boxplot'])
            if(sel == 'Histogram'):
                st.header('Univariate Analysis')
                histogram(df)
            if(sel == 'Boxplot'):
                st.header('Univariate Analysis')
                boxplot(df)
            if(sel == 'PDF (Probability Distribution Function)'):
                st.header('Univariate Analysis')
                probabilty(df)
        if(sel1 == 'Categorical'):
            sel2 = st.sidebar.selectbox('Univariate Analysis (For Non Categorical variables',['--Select One--','Countplot','Piechart'])
            if(sel2 == 'Countplot'):
                st.header('Univariate Analysis')
                countplot(df)
            if(sel2 == 'Piechart'):
                st.header('Univariate Analysis')
                piechart(df)

    if(st.sidebar.checkbox('Bivariate Analysis')):
        sel3 = st.sidebar.selectbox('Select type',['-- Select One--','ScatterPlot','HexbinPlot','BoxPlot'])
        if(sel3 == 'ScatterPlot'):
            st.header('Bivariate Analysis')
            scatter_plot(df)
        if(sel3 == 'HexbinPlot'):
            st.header('Bivariate Analysis')
            hexbin_plot(df)
        if(sel3 == 'Boxplot'):
            st.header('Bivariate Analysis')
            box_plot(df)

    if(st.sidebar.checkbox('Multivariate Analysis')):
        sel3 = st.sidebar.selectbox('Select type',['-- Select One--','Pairplot','Heatmap'])
        if(sel3 == 'Pairplot'):
            st.header('Multivariate Analysis')
            pair_plot(df)
        if(sel3 == 'Heatmap'):
            st.header('Multivariate Analysis')
            heat_map(df)






def main():
    
    df = load_data(dataset_loc)
    sidebar(df)
    select_box(df)

if(__name__ == '__main__'):
    main()