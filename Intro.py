import streamlit as st
from PIL import Image

st.title("Cocina Inteligente")
st.subheader("Página por Jorge, Kely y Juan <3")
image = Image.open('cocina.jpg')

st.image(image)
