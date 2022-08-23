import streamlit as st
import pandas as pd
import numpy as np
import pickle


#st.title('Top 100 Books')
st.set_page_config(
    page_title="Books Recommendation System",
    page_icon="👋",
)
st.write('# Welcome to Bookshelf')
st.write("## Most Popular Books 📗")

# html_temp = """
# <div style="background-color:tomato;padding:10px">
# <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App</h2>
# </div>
# """


df1=pickle.load(open('Books.pkl','rb'))
df=df1.iloc[:100]
listofimages=df['Image-URL-M'].to_list()
df['caption']='Title: '+df['Book-Title']
df['caption']=df['caption']+'\n'+'Author: '+df['Book-Author']
df['caption']=df['caption']+'\n'+'\n'+'avg-rating: \n'+np.round(df['avg-rating'],2).astype(str)


st.image(listofimages,caption=df['caption'].to_list(),width=100,use_column_width=1000)
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone"))
#st.write(np.vsplit(np.array([listofimages]),3))
    #st.write(row['Image-URL-M'])
    #image = Image.open(row['Image-URL-M'])
#     st.image(row['Image-URL-M'])
#     st.write(row['Book-Title'])
#     st.write(row['Book-Author'])
#     st.write(row['avg-rating'])
    #st.image(image, caption = 'This is a picture', use_column_width = True)
    

# save the input text in the variable 'name'
# first argument shows the title of the text input box
# second argument displays a default text inside the text input area

