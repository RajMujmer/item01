import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
st.title("This is for practice purpose")
st.header("Exploring Data....")
st.subheader("Here")
Name = ["Aditya", "Ganesh", "Shivam"]
df = pd.DataFrame(Name)
st.write("Here is the data : ", df)


st.markdown("# This is a level 1 heading")
st.text("Ab Samajh aya ki nahi")


name = st.text_input("Enter your name:", placeholder="e.g., Charlie")
age = st.slider("Select your age:", 0, 100, 25, help="This slider controls your age.")

option = st.selectbox("Choose a fruit:", ["Apple", "Banana", "Cherry"], index=1)


def format_name(name, prefix="Dr."):
    st.session_state['formatted_name'] = f"{prefix} {name.upper()}"

st.text_input("Enter your name:", key="raw_name", on_change=format_name, args=("Mr.",)) # Note: args is a tuple
st.write(f"Formatted Name: {st.session_state.get('formatted_name', '')}")



def update_message(text, suffix="!!!"):
    st.session_state['message'] = text + suffix

st.text_input("Enter a message:", key="input_message", on_change=update_message, kwargs={"suffix": "..."})
st.write(f"Your message: {st.session_state.get('message', '')}")
