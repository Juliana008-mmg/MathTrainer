import streamlit as st

st.title("Cours de mathématiques")

st.header("Équation du premier degré")

st.write("""
Une équation du premier degré est de la forme :

ax + b = c
""")

st.header("Équation du second degré")

st.latex("ax^2 + bx + c = 0")

st.write("""
Le discriminant est :

Δ = b² - 4ac
""")