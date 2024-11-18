import streamlit as st
import pandas as pd
import random

# Load the CSV file
@st.cache
def load_data():
    return pd.read_csv("names.csv")

# Load data
data = load_data()

# Page title and header
st.set_page_config(page_title="Who will handle the huddle?", page_icon="🌟", layout="centered")
st.title("🌟 **Huddle Leader Picker** 🌟")
st.subheader("Let's find out who will lead next week's huddle!")

# Add a decorative banner
st.markdown(
    """
    <div style="background-color:#f7f7f9;padding:10px;border-radius:10px;margin-bottom:20px;">
        <h4 style="color:#4CAF50;text-align:center;">Empowering Collaboration for the Week Ahead!</h4>
    </div>
    """,
    unsafe_allow_html=True,
)

# Button to pick a random name
if st.button("✨ Pick the Huddle Leader ✨"):
    random_name = random.choice(data['Agents'])
    st.markdown(
        f"""
        <div style="background-color:#ffeb3b;padding:15px;border-radius:10px;margin-top:20px;">
            <h2 style="text-align:center;color:#000;">🎉 Next week's huddle will be handled by:</h2>
            <h1 style="text-align:center;color:#4CAF50;">{random_name}</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.info("Click the button to pick a random huddle leader!")
    
    unsafe_allow_html=True,
)
