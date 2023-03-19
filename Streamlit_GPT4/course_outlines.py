import openai
import streamlit as st
import pandas as pd
import numpy as np

openai.api_key = "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"

# Define function to generate an outline
def generate_outline_GPT(context, engine, max_tokens, temperature):
    prompt = f"Generate an outline for an online course on {context}"
    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=temperature,
    )
    outline = response.choices[0].text.strip()
    return outline

def generate_outline_chatGPT(context, model, max_tokens, temperature):
    prompt = f"Generate an outline for an online course on {context}"
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "system", "content": "You are a helpful teaching assistant who is skilled in drafting outlines, both in English and Spanish, for succesful online courses."},
                  {"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    outline = response['choices'][0]['message']['content'].strip()
    return outline

# Define session state variables
if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 256
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.5
if "engine" not in st.session_state:
    st.session_state.engine = "text-davinci-002"

# Set app title and instructions
st.title("Online Course Outline Generator")
st.write("Enter some context for your online course, and we'll generate an outline for you!")

# Add a sidebar for controlling model parameters
with st.sidebar:
    st.write("## Model Parameters")
    st.session_state.max_tokens = st.slider("Max Tokens", min_value=32, max_value=2048, value=st.session_state.max_tokens)
    st.session_state.temperature = st.slider("Temperature", min_value=0.1, max_value=1.0, value=st.session_state.temperature, step=0.1)
    st.session_state.engine = st.selectbox("Engine", 
                                           ["GPT-3", "chatGPT-3.5", "chatGPT-4"], 
                                           index=["text-davinci-003", "gpt-3.5-turbo", "gpt-4"].index(st.session_state.engine))

# Get user input and generate outline
context = st.text_input("Enter context for your course here:")
if context:
    if st.button("Generate Outline"):
        if st.session_state.engine == "GPT-3":
            outline = generate_outline_GPT(context, st.session_state.engine, st.session_state.max_tokens, st.session_state.temperature)
            
        elif st.session_state.engine == "chatGPT-3.5":
            outline = generate_outline_chatGPT(context, st.session_state.engine, st.session_state.max_tokens, st.session_state.temperature)
            
        elif st.session_state.engine == "chatGPT-4":
            outline = generate_outline_chatGPT(context, st.session_state.engine, st.session_state.max_tokens, st.session_state.temperature)

        st.write("## Generated Outline")
        st.write(outline)
