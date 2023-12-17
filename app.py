from nlp_bot import pred_class, get_response, words, data, classes
import streamlit as st
import time
import tensorflow as tf

st.title('Chatbot 🤖')
st.write(
        "Welcome to the Data Science Chatbot!👋 This chatbot is designed to assist you with various data science topics.😎 "
        "Whether you're a beginner or an experienced data scientist, feel free to ask questions and explore the world of data science.🤓"
    )

the_word_you = '<h4>You: </h4>'

st.markdown(f'{the_word_you}', unsafe_allow_html=True)
message = st.text_input('')

intents = pred_class(message.lower(), words, classes)
result = get_response(intents, data)

# disply the answer as it is being written in real time
def typewriter(text, speed):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text)
        time.sleep(1 / speed)

the_word_bot = '<h4>Bot: </h4>'
st.markdown(f'{the_word_bot}', unsafe_allow_html=True)
typewriter(result, 10)

#st.title("About Data Science Chatbot")



# might delete that
st.header("How to Use the Chatbot")

st.markdown(
        """
        1. **Ask Questions:** Simply type your data science-related questions into the chatbox on the left side of the page.
        The chatbot will do its best to provide helpful and informative responses.

        2. **Feedback:** Your feedback is valuable! If you have suggestions, encounter issues, or want to share your thoughts, 
        use the feedback form provided.

        3. **Explore Examples:** Check out the provided examples to see how to use various data science tools and techniques.
        """
    )

st.header("Important Notes")

st.markdown(
        """
        - This chatbot is designed for educational purposes and may not cover all aspects of data science.

        - The chatbot's responses are based on pre-existing knowledge up to its last training cut-off. It may not have 
        real-time information on the latest developments.

        - The code snippets provided are for educational purposes. Always review and adapt them based on your specific 
        use case and requirements.

        - Your privacy is important. Avoid sharing sensitive or personal information in the chat.

        - Have fun exploring the world of data science with the chatbot!
        """
    )

st.header("Feedback and Support")

st.markdown(
        """
        Your feedback is essential for improving the chatbot. If you encounter issues, have suggestions, or want to share your experience,
        please use the feedback form provided in the app.

        Thank you for using the Data Science Chatbot! Happy learning!
        """)
footer="""<style>
a:link , a:visited{
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
text-align: center;
}
</style>
<div class="footer">
<p>For Feedback: 
<a href="https://www.linkedin.com/in/zaid-allwansah/" target="_blank">Zaid</a> |
<a href="https://www.linkedin.com/in/layan-bilbeisi/" target="_blank">Layan</a>
</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)