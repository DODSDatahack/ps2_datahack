API_KEY='YOUR_API_KEY'
import openai
import os
import streamlit as st
os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key'] 
st.title("DODS AI")
prompt= st.text_input("How can I help you")
keep_prompting= st.button("Go")
if keep_prompting:
    response=openai.Completion.create(engine='text-davinci-003',prompt=prompt, max_tokens=200)
    st.write(response['choices'][0]['text'])
    keep_prompting = False

