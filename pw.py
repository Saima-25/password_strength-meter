import streamlit as st
import re
import random
import string

st.title("🔑 Password Strength Checker")
st.subheader("Check your password strength and get security tips! 🔐")

st.image("pw_image.webp", caption="Password Strength Meter UI", width=300)

blacklist = ["password", "123456", "qwerty", "abc123", "Admin123"]
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*?/.,"
    return "".join(random.sample(chars, 12))

def check_pw_strength(password):
    if password in blacklist:
        st.error("❌ This is a common password and easy to be hack. Please choose a different one.")
        return
    score = 0
    if (len(password)) >= 12:
        score += 2
    elif(len(password)) >= 8:
        score += 1.5
    else:
        st.error("❌ password should be consist on minimum 8 characters long")  
        
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password ):
        score += 1
    else:
        st.error(" ❌ Password should contain both upper and lower case.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        st.error("❌ Password should contain atleast one digit (0-9).")
        
    if re.search(r"[!@#$%^&*?/.,]", password):
        score += 1
    else:
        st.error("❌ special character (!@#$%^&*?/.,) must be include")
        
    if score >=4:
        st.success("✅ Strong Password 🛡!")
        st.progress(100)
        st.info("Your password meets all the security requirements.")
    elif score >=3 :
        st.warning("⚠ Moderate Password!- add some features to make it secured ")
        st.progress(75)    
        st.info("Your password is adequate but consider using a stronger password.")  
    else:
        st.warning("❌ Weak Password 🎃 - improve your password by using above suggessions")
        st.progress(25)
        st.info("Your password is not secure enough. Consider using a stronger password.")
        
password = st.text_input("Enter your password:")
if password:
        check_pw_strength(password)
if st.button("Generate Strong Password 🔄"):
        st.info(f"🔹 Suggested Strong Password: `{generate_password()}` (Copy & Use)")   
        
