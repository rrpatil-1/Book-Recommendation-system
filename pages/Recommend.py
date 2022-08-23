import streamlit as st
import pandas as pd
import numpy as np
import pickle
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords

similarity_score=pickle.load(open('similarity_score.pkl','rb'))
pt=pickle.load(open('pt.pkl','rb'))
df1=pickle.load(open('Books.pkl','rb'))

def recommend(book,df1):
    try:
        vOutcome='FAIL:Default-->recommend'
        index=np.where(pt.index==book)[0][0]
        similar_item=sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
        data=[]
        temp_df=df1[df1['Book-Title']==pt.index[index]]
        item1=[]
        item1.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item1.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item1.extend(list(np.round(temp_df.drop_duplicates('Book-Title')['avg-rating'].values,2)))
        item1.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item1)
        for i in similar_item:
            item=[]
            temp_df=df1[df1['Book-Title']==pt.index[i[0]]]
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
            item.extend(list(np.round(temp_df.drop_duplicates('Book-Title')['avg-rating'].values,2)))
            item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
            data.append(item)
    except IndexError as e:
        st.write('Please type correct book name,check spelling error')
    else:
        vOutcome=data
    finally:
        
        return vOutcome
    
def fetchresult(data):
    try:
        for row in data:
            if row:
                BookTitle=row[0]
                Author=row[1]
                avgrating=round(row[2])
                ImageURL=row[3]
                st.image(ImageURL)
                st.markdown(f'Book-Title: {BookTitle}')
                st.markdown(f'Author: {Author}')
                st.markdown(f'Avg-Rating: {avgrating}')
    except IndexError as e:
        st.write('Please type correct book name,check spelling error')
        st.write(e)

def get_book_name(strbook,pt):
    try:
        
        vOutcome='FAIL:Default--get_book_name'
        punk=list(string.punctuation)
        stop=stopwords.words('english')
        badword=punk+stop
        
        bookname=strbook.lower()
        listofword=[word for word in word_tokenize(bookname) if word not in badword]
        bookswithword=''
        if listofword:
            for word in listofword:
                bookswithword=pt[pt.index.str.contains(word)]
                if len(bookswithword)>0:
                    break
                    
    except:
        vOutcome= 'FAIL:get_book_name '+str(sys.exe_info())
    else:
        if len(bookswithword)>0:
            vOutcome=bookswithword.index[0]
        else:
            vOutcome='FAIL:No book found'
    finally:
        return vOutcome
        
        
    
            
name = st.text_input("Enter Name of Book", "Type Here ...")

# display the name when the submit button is clicked
# .title() is used to get the input text string
if __name__=='__main__':
    if(st.button('Submit')): 
        result = name.title()
        strInput=''.join(result.split())

        if strInput.isalnum() or strInput.isdigit():
            result=result.lower()
            bookname=get_book_name(result,pt)
            if not str(bookname).startswith('FAIL:'):

                #st.write(get_book_name(result,pt))
                data=recommend(bookname,df1)
                if type(data)!=str:
                    fetchresult(data)
            else:
                if 'No book found' in bookname:
                    st.info('Check Spelling error,Misspell word',icon='ℹ')
                else:
                    st.warning(bookname,icon='⚠️')
        else:
            st.info('Please provide correct input',icon='ℹ')

    
	