##################################Importing Libraries##################################
import streamlit as st
import random
import string

##################################Intialized a variable password ##################################

password = ""

##################################Intialized a Streamlit Page Configurations##################################

st.set_page_config("Passwort Generator" , "🔐")
st.markdown("<h1 style='font-size: 40px;'>🔐 Random Password Generator</h1>", unsafe_allow_html=True)
multiselect = st.multiselect("Select the characters that needs to be includes in the password", ["Uppercase", "Lowercase", "Numbers", "Special Characters"])
slider = st.slider("Password Length", 1, 50, 10)
button = st.button("Generate Password")


##################################Password Generation Logic##################################
if button == True:
    try:
        if "Uppercase" in multiselect:
            password += string.ascii_uppercase
        if "Lowercase" in multiselect:
            password += string.ascii_lowercase
        if "Numbers" in multiselect:
            password += string.digits
        if "Special Characters" in multiselect:
            password += string.punctuation
    except Exception as e:
        st.error("Please select atleast one option")
    try:

        password = "".join(random.choice(password) for i in range(slider))
        st.markdown(f"<h2 style='font-size: 30px;'>Here is your generated password</h2>", unsafe_allow_html=True)
        st.code(password, language='')
    except IndexError as e:
        st.error("Please select atleast one option from the charecterset")
    except TypeError as e:
        st.error("Oop's something went wrong")

##################################Footer##################################
