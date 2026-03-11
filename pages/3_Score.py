import streamlit as st

st.title("Score")

if "score" in st.session_state:
    st.write("Votre score :", st.session_state.score)
    st.write("Questions :", st.session_state.total)
else:
    st.write("Aucun exercice fait pour le moment.")