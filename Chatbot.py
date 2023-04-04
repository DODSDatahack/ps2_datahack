API_KEY='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'
import openai
import os
import streamlit as st
i=0
os.environ['OPENAI_Key']=API_KEY
openai.api_key=os.environ['OPENAI_Key'] 
st.title("DODS AI")
prompt= st.text_input("How can I help you")
keep_prompting= st.button("Go")
if keep_prompting:
    response=openai.Completion.create(engine='text-davinci-003',prompt=prompt, max_tokens=200)
    st.write(response['choices'][0]['text'])
    keep_prompting = False

