import re
import streamlit as st

# Styling the page
st.set_page_config(page_title="Password Strength Mechanism - Iqra Kalim", page_icon="🔋", layout="centered")

# Custom CSS
st.markdown("""
<style>        
.main {text-align: center;}
.stTextInput {width: 60% !important; margin: auto;}
.stButton button {
    width: 50%;
    background-color: #F4A460;
    color: #7B68EE;
    font-size: 18px;
}
.stButton button:hover {
    background-color: #e129d6;
}
</style>
""", unsafe_allow_html=True)

# Title and description
st.title("🔌🔋 Password Strength Mechanism 💹")
st.write("This app aims to ensure a secure check of your guarded treasure: PASSWORD so that it remains 🚨SECURE🚨")

# Text input for password
password = st.text_input("Enter your password", type="password", help="Use a mix of characters to create a strong password 💪🏼")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("😖 Required a password of **at least 8 characters** ‼️")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("👋🏼 You MUST have **BOTH Uppercase & Lowercase characters** ‼️")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🎱 Your password MUST contain **At least 1 digit (0-9)** 💯")

    if re.search(r"[!@#$%^&*()_+]", password):
        score += 1
    else:
        feedback.append("🔑 Your password MUST contain **Special Character (!@#$%^&*()_+)** ⚙️")

    # Strength results
    if score == 4:
        st.success("🎉 Your password is **STRONG** 💪🏼")
    elif score == 3:
        st.info("🚧 Considerably better... but **ADD More Characters** to STRENGTHEN Build! 🛠️")
    else:
        st.error("🤒 **WEAK password** 🤒, please try referring to the Solution-board below")
        with st.expander("😇 **Solution to Strengthen Password** ✅"):
            for item in feedback:
                st.write(f"- {item}")

# Button to check strength
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please ENTER a Password ☠️!!FIRST!!☠️")
