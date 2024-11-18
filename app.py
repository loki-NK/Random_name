import streamlit as st
import pandas as pd
import random

# Load the CSV file
@st.cache
def load_data():
    return pd.read_csv("names.csv")

# Load data
data = load_data()

# Title
st.title("Who will led the next week's huddle?")

# Button to pick a random name
if st.button("Pick a Random Name"):
    random_name = random.choice(data['Agents'])
    st.write(f"🎉 Next week huddle will be handled by: **{random_name}**")

