import streamlit as st
from openai import OpenAI
st.title("Provided with love by of Lubna Kent")

note= (''' All three pages will provided similar response \n 1. "Ask Kamila a Question" page makes a call to OpenAI API to get an answer to a question and provides the response received from OpenAI. \n 2. "Ask Kamila to Compute Percent Complete" page makes a call to OpenAI API and OpenAI uses a "custom in-house built" function sent with the call to compute the percent complete.\n3. "Compute Percent Complete" page does not make a call to OpenAI API and uses a custom in-house function to compute percent complete. \n''')
function_calling = ('''**Learn more about function calling by accessing the link below:\n https://platform.openai.com/docs/guides/function-calling''')
blank_lines = ('''\n\n''')
st.markdown(note)
st.markdown(blank_lines)
#st.markdown(f"**{function_calling}**")
