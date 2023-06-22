import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
import os

# keys 
os.environ['OPENAI_API_KEY'] = st.secrets['OPENAI_API_KEY']

# setting the model up and prompting it
template = """
    Below is a text provided by a user.
    Your goal is to:
    - Summarize the input text to one / two sentences
    - Convert the gender of the user into an emoji and include in the emoji translation of the sentence
    - Convert the summarized text to a set of emojis that describe the essence of the sentence

  Here are some examples of converting gender of the user into an emoji:
    - Male = 👨
    - Female = 👩

    Here are some examples of converting sentences into emojis:
    - Sentence: Me (male) and my dog are going to the beach
    - Emojis: 👨🐕  ➡️🏖️

    Below is the text and gender:
    TEXT: {text}
    GENDER: {gender}
    
    YOUR  RESPONSE:

"""

prompt = PromptTemplate(
    input_variables=['gender', 'text'],
    template= template
)

def load_LLM():
    llm = OpenAI(temperature= 1 )
    return llm

llm = load_LLM()


# streamlit
st.set_page_config(page_title='Emoji translator ', page_icon=':robot:')
st.header('Express yourself in emojis')
st.markdown('Select your gender and translate sentences about how you feel into emojis')


st.markdown('### Enter feeling to translate into emojis')

col1, col2 = st.columns(2)

with col1:
    option_gender = st.selectbox(
      'what is your gender:',
      ('Male', 'Female', 'Undefined') )

def get_text():
    input_text = st.text_area(
    label='', placeholder="Feelings to translate..", key='text_input')
    return input_text
    
text_input = get_text()

st.markdown("### Your emoji'ed text")

if text_input:
    prompt_with_text = prompt.format(gender = option_gender, text = text_input)
    translated_text = llm(prompt_with_text)
    st.write(translated_text)


