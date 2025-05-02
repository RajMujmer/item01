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

#######################################################################################

with st.form("my_form"):
    name = st.text_input("Your name:")
    ID = st.text_input("Your ID")
    Height = st.slider("Your height:", 100, 250)
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(f"Name:  {name}, "    ", ID:  {ID}, "    ", HEIGHT:  {Height}cm")


#######################################################################################

data = ["Feature A", "Feature B", "Feature C"]
cols = st.columns(len(data))

for i, feature in enumerate(data):
    with cols[i]:
        st.subheader(feature)
        st.checkbox(f"Enable {feature}")

######################################################################################

import streamlit as st
import pandas as pd
import numpy as np

tab1, tab2, tab3 = st.tabs(["Data Exploration", "Visualization", "Settings"])

with tab1:
    st.header("Data")
    data = pd.DataFrame(np.random.rand(10, 2), columns=['x', 'y'])
    st.dataframe(data)

with tab2:
    st.header("Chart")
    st.line_chart(data)

with tab3:
    st.header("Preferences")
    color = st.selectbox("Select color:", ["red", "green", "blue"])
    st.write(f"Selected color: {color}")


