import streamlit as st
from PIL import Image
import numpy as np
import random

st.title("Human-AI Story Illustration Assistant")

scene = st.text_input(
    "Describe the scene",
    "Hanuman flying over the ocean"
)

artist_image = st.file_uploader("Upload your sketch")

layouts = [
"Low angle heroic perspective",
"Diagonal action composition",
"Wide cinematic landscape",
"Triangular dramatic layout"
]

def extract_colors(image):

    img = np.array(image)
    pixels = img.reshape(-1,3)

    idx = np.random.choice(len(pixels), 5)
    colors = pixels[idx]

    return colors

if artist_image:

    img = Image.open(artist_image)

    st.image(img, width=300)

    st.header("AI Color Suggestions")

    colors = extract_colors(img)

    for c in colors:
        st.write(f"RGB: {c}")

    st.header("AI Composition Ideas")

    for i in range(3):
        st.success(random.choice(layouts))
