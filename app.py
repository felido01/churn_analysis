import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

df = px.data.iris()
st.title('Iris Species-Dataset Short Overview')
# st.markdown("<h4> Enter your Name</h2>", unsafe_allow_html=True)
# st.write("Enter your Name")
st.markdown("<b style= 'color: orange'> This web App is Aimed to aid understanding in the dataset- Iris </b>", unsafe_allow_html=True)
Input=st.text_input("Enter Your Name")
if Input:
    # st.write('Welcome', Input,"!")
    st.write("Let's Start", Input)
drop=st.selectbox("Select specie to explore",df['species'].unique())

filter_df=df[df['species']==drop]
# col1,spacer,col2=st.columns([3,0.2,5])

# with col1:




# with col2:
fig = px.scatter(
    filter_df,
    x='sepal_length',
    y='sepal_width',
    color_discrete_sequence=['orange'],
    marginal_x='box',
    marginal_y='violin'
    # marginal_y='histogram'
)

fig.update_layout(
    # bargap=0.3,
    width=500,   # make it wider
    height=500    # make it taller
)

st.plotly_chart(fig,use_container_width=True)

if  st.checkbox('Show Dataframe'):
    st.dataframe(filter_df, use_container_width=True)

column=df[["sepal_length","sepal_width","petal_length","petal_width"]]

avg_inp=st.text_input(
    'Average'
)
if avg_inp=='sepal_length':
    st.write(filter_df['sepal_length'].mean().round(2))
if avg_inp=='sepal_width':
    st.write(filter_df['sepal_width'].mean().round(2))
if avg_inp=='petal_length':
    st.write(filter_df['petal_length'].mean().round(2))
if avg_inp=='petal_width':
    st.write(filter_df['petal_width'].mean().round(2))
if avg_inp=="":
    st.write("")
if avg_inp not in ['sepal_length','sepal_width','petal_width','petal_length',""," "]:
    st.markdown("<h6 style=color:red>Please provide a valid column name from the dataset.</h6>", unsafe_allow_html=True)

