import streamlit as st
import re

st.title("🔑 Password Strength Checker")
st.subheader("Check your password strength and get security tips! 🔐")

st.image("pw_image.webp", caption="Password Strength Meter UI", width=300)

def check_pw_strength(password):
    score = 0
    
    # check length
    if len(password) >= 8: 
      score += 1
    else:
        st.error( "❌ password should be at least 8 characters long") 
        
    # check for uppercase letters and lowercase as well
    if (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        score += 1
    else:
        st.error(" ❌ password should contain both upper and lower case letters") 
        
    # check digit
    if (re.search(r"\d", password)):
        score += 1
    else:
        st.error("❌ password  should contain one digit (0-9) atleast ") 
        
    # check special character
    if (re.search(r"[!@#$%^&*?/.,]", password)):
        score += 1
    else:
        st.error("❌ special character (!@#$%^&*?/.,) must be include") 
        
        # check strength or rating strength
    

    if score == 4:
        st.success("✅ Strong Password 🛡! ")
        st.progress(100)
    elif score == 3:
        st.warning("⚠ Moderate Password!- add some features to make it secured ")
        st.progress(75)
    else:
        st.warning("❌ Weak Password 🎃 - make your password by using above suggessions")
        st.progress(25)
                
    # user input
password = st.text_input("**Enter your password:**")
if password:
    check_pw_strength(password)
        