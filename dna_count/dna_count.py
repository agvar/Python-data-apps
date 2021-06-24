import pandas as pd
import streamlit as st
import altair as alt

dict={}
nucleo_list={'A','T','G','C'}
st.write('# DNA necleotide count App')
st.write('***')

#read input DNA from the web app
read_input=st.text_area("Input DNA sequence",height=250)

#replace line feeds,carriage returns and spaces and convert to upper
cleansed_input=read_input.replace('\n','').replace('\r','').replace(' ','').upper()

#check if DNA sequence entered is valid
if cleansed_input and not(set(cleansed_input).issubset(nucleo_list)):
    st.error("DNA sequence needs to be a sequence of A,T,G,C ")
else:
    #create a dictionary with the nucleotide counts
    for letter in cleansed_input:
        dict[letter]=dict.setdefault(letter,0)+1

st.write(pd.DataFrame([dict]))
df=pd.DataFrame.from_dict(dict,orient='index')
st.write(df)
df.reset_index(inplace=True)
df=df.rename(columns={'index':'nucleotide',0:'count'})
st.write("df is :",df)

#create a chart

st.subheader('Bar Chart')
p=alt.Chart(df).mark_bar().encode(x='nucleotide:O', y='count:Q').properties(width=alt.Step(100))
st.write(p)