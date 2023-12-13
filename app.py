from itertools import count
from turtle import title
import streamlit as st
import streamlit.components.v1 as components

from chatbot import *

title = '''<h1>A Data Science Chatbot</h1>'''

st.markdown(title, unsafe_allow_html=True)
st.markdown('this is only a temporary chatbot, but the real one will be deployed soon')

st.markdown('Bot: hello I am a data science chatbot, ask me anything!')



# loading the data
knowledge_base:dict = load_knowledge_base('knowledge_base1.json')

user_input = st.text_input('You: ')
            
# this will look for the best match inside of our json file
best_match = find_best_match(user_input, [q['question'] for q in knowledge_base['questions']])

if best_match:
    answer = get_answer_for_question(best_match, knowledge_base)
    st.markdown('Bot: ')
    st.markdown(answer)
else:
    st.markdown("Bot: I don't know the answer, can you teach me?")
    new_answer = st.text_input('type the answer')
    variable = new_answer
    knowledge_base['questions'].append({'question': user_input, 'answer': variable})
    save_knowledge_base('knowledge_base1.json', knowledge_base)