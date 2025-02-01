import streamlit as st
from transformers import pipeline

# Initialize the models
model_1 = pipeline("text-generation", model="gpt2")  # Example GPT-2
model_2 = pipeline("text-generation", model="EleutherAI/gpt-neo-2.7B")  # Example GPT-Neo
model_3 = pipeline("text-to-text-generation", model="t5-base")  # Example T5

models = {
    "GPT-2": model_1,
    "GPT-Neo": model_2,
    "T5": model_3
}

# Title of the app
st.title("Drug Debate Chatbot")

# Input fields for patient condition and drug
condition = st.text_input("Enter your condition:")
drug = st.text_input("Enter the prescribed drug:")

# Dropdown to select the first and second model
model_1_select = st.selectbox("Select first model:", ["GPT-2", "GPT-Neo", "T5"])
model_2_select = st.selectbox("Select second model:", ["GPT-2", "GPT-Neo", "T5"])

# Button to trigger the debate
if st.button("Start Debate"):
    model_1_choice = models[model_1_select]
    model_2_choice = models[model_2_select]

    # Define prompts for the models
    prompt_1 = f"Debate the pros and cons of the drug {drug} for treating {condition}. Model 1, argue in favor."
    prompt_2 = f"Debate the pros and cons of the drug {drug} for treating {condition}. Model 2, argue against."

    # Generate the responses
    response_1 = model_1_choice(prompt_1, max_length=200, num_return_sequences=1)
    response_2 = model_2_choice(prompt_2, max_length=200, num_return_sequences=1)

    # Display the results
    st.subheader(f"Model 1 ({model_1_select}) - Pro Side")
    st.write(response_1[0]['generated_text'])
    
    st.subheader(f"Model 2 ({model_2_select}) - Con Side")
    st.write(response_2[0]['generated_text'])
