import streamlit as st

st.title("First App using Streamlit🎉🎉")
openion=st.text_input("Enter here your openion about this framework")
if openion:
    st.write(openion,"👍🎉")