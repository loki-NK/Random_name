import streamlit as st
import pandas as pd
import random

# Set page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Who will handle the huddle?", page_icon="🌟", layout="centered")

# Load the CSV file
@st.cache
def load_data():
    return pd.read_csv("names.csv")

# Load data
data = load_data()

# Page title and header
st.title("🌟 **Huddle Leader Picker** 🌟")
st.subheader("Let's find out who will lead next week's huddle!")

# Button to pick a random name
if st.button("✨ Pick the Huddle Leader ✨"):
    random_name = random.choice(data['Agents'])
    st.markdown(
        f"""
        <div style="background-color:#05006D;padding:20px;border-radius:15px;margin-top:25px;">
            <h2 style="text-align:center;color:#03A94A;">🎉 Next week's huddle will be handled by:</h2>
            <h1 style="text-align:center;color:#FFFFFF;">{random_name}🙌</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.balloons() 
else:
    st.info("Click the button to pick a random huddle leader!")
