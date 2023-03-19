import openai
import streamlit as st


openai.api_key = "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"


def compute_cost(tokens, engine):
    
    model_prices = {"text-davinci-002": 0.02, 
                    "gpt-3.5-turbo": 0.002, 
                    "gpt-4": 0.03}
    model_price = model_prices[engine]
    
    if engine == "text-davinci-002":
        cost = (tokens / 1000) * model_price
    else:
        cost = (tokens / 1000) * model_price
    return cost


def generate_outline(context, engine, max_tokens, temperature):
    prompt = f"Generate an outline for an online course on {context}"
    
    if st.session_state.engine == "text-davinci-002":
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
        tokens_used = response.usage.total_tokens
        
    else:
        response = openai.ChatCompletion.create(
        model=engine,
        messages=[{"role": "system", "content": "You are a helpful teaching assistant who is skilled in drafting outlines, both in English and Spanish, for succesful online courses."},
                  {"role": "user", "content": prompt}],
        max_tokens=max_tokens,
        temperature=temperature,
        )
        outline = response['choices'][0]['message']['content'].strip()
        tokens_used = response.usage.total_tokens
        
    return (outline, tokens_used)

# Define session state variables
if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 256
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.5
if "engine" not in st.session_state:
    st.session_state.engine = "text-davinci-002"
if "tokens_used" not in st.session_state:
    st.session_state.tokens_used = 0

# Set app title and instructions
st.title("Online Course Outline Generator")
st.write("Enter some context for your online course, and we'll generate an outline for you!")

# Add a sidebar for controlling model parameters
with st.sidebar:
    st.write("## Model Parameters")
    st.session_state.max_tokens = st.slider("Max Tokens", min_value=32, max_value=2048, value=st.session_state.max_tokens)
    st.session_state.temperature = st.slider("Temperature", min_value=0.1, max_value=1.0, value=st.session_state.temperature, step=0.1)
    st.session_state.engine = st.selectbox("Engine", 
                                           ["text-davinci-002", "gpt-3.5-turbo", "gpt-4"])

    st.write("## Tokens Used")
    st.write(st.session_state.tokens_used)
    st.info(f"So far spent: ${compute_cost(st.session_state.tokens_used, st.session_state.engine)}")
    
# Get user input and generate outline
context = st.text_input("Enter context for your course here:")
if context:
    try:
        if st.button("Generate Outline"):

            outline, tokens_used = generate_outline(context, 
                                        st.session_state.engine, 
                                        st.session_state.max_tokens, 
                                        st.session_state.temperature)
            
            st.session_state.tokens_used += tokens_used
            st.write("## Generated Outline")
            st.write(f" ---- OUTLINE GENERATED ---- \n\n {outline}")
            st.info(f"Tokens used: {tokens_used}. Total tokens used: {st.session_state.tokens_used}")
            st.info(f"Total cost: ${compute_cost(st.session_state.tokens_used, st.session_state.engine)}")
            
    except Exception as e:
        st.error(e)
        
if not context:
    st.info("Please enter some context for your online course in the text box")