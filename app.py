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
st.title("Random Name Picker")

# Button to pick a random name
if st.button("Pick a Random Name"):
    random_name = random.choice(data['Name'])
    st.write(f"🎉 Random Name: **{random_name}**")

st.write("Upload a new CSV file below (optional):")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("✅ File uploaded successfully!")
