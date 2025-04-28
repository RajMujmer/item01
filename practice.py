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


name = st.text_input("Enter your name:", label="Your Name", placeholder="e.g., Charlie")
age = st.slider("Select your age:", 0, 100, 25, help="This slider controls your age.")
