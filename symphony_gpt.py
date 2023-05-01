import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

from song_template import prompt


prompt = PromptTemplate(
    input_variables=["notes", "musician1", "attribute1", "musician2", "attribute2"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="SymphonyGPT", page_icon=":music:")
st.header("SymphonyGPT")


st.image(image='symphony.jpg')
st.markdown(" This tool \
                is powered by [LangChain](https://langchain.com/) and [OpenAI](https://openai.com). View Source Code on [Github]()")


st.markdown("## Select Influences and Attributes")



col1, col2 = st.columns(2)
with col1:
    option_musician1 = st.text_input(
        'Musical Influence #1',
        key="musician1_selectbox"
    )
    
with col2:
    option_attribute1 = st.text_input(
        'What particular attribute?',
        key="attribute1_selectbox"
    )

with col1:
    option_musician2 = st.text_input(
        'Musical Influence #2',
        key="musician2_selectbox"
    )
    
with col2:
    option_attribute2 = st.text_input(
        'What particular attribute?',
        key="attribute2_selectbox"
    )


def get_text():
    input_text = st.text_area(label="Additional Notes", label_visibility='collapsed', placeholder="Your Email...", key="email_input")
    return input_text

notes_input = get_text()

if len(notes_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-34hscc88chbs...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

st.button("*Get Report*", type='secondary', help="Click to see song report.")



if notes_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    #llm = load_LLM(openai_api_key=openai_api_key)
    llm = OpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, max_tokens=2000)

    prompt_with_options = prompt.format(notes=notes_input, musician1=option_musician1, attribute1=option_attribute1, musician2=option_musician2, attribute2=option_attribute2)

    song_report = llm(prompt_with_options)

    st.write(song_report)