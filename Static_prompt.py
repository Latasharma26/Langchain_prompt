from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
st.header("Static Prompt with Langchain and Streamlit")
st.header("Research Tool")
user_input = st.text_input("Enter your research topic:")
model = ChatOpenAI(model='gpt-4', temperature=1.5)

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)


