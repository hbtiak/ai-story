import streamlit as st
from PIL import Image
import random

st.title("Human-AI Story Illustration Lab")

scene = st.text_input(
    "Describe the story scene",
    "Hanuman jumping across the ocean to Lanka"
)

style = st.selectbox(
    "Art style",
    ["Comic Book", "Caricature", "Epic Painting", "Watercolor"]
)

mood = st.selectbox(
    "Mood",
    ["Heroic","Divine","Battle","Sunset"]
)

artist_image = st.file_uploader("Upload your sketch")

if artist_image:
    img = Image.open(artist_image)
    st.image(img, width=300)

st.header("AI Composition Ideas")

layouts = [
"Low angle heroic perspective",
"Diagonal action composition",
"Wide cinematic frame",
"Triangular dramatic layout"
]

if st.button("Generate Composition Ideas"):
    for i in range(4):
        st.success(random.choice(layouts))

st.header("AI Color Suggestions")

palettes = {
"Heroic": ["gold","deep red","royal blue"],
"Divine": ["white","light blue","gold"],
"Battle": ["black","crimson","dark purple"],
"Sunset": ["orange","pink","violet"]
}

if st.button("Generate Color Palette"):
    st.write(palettes[mood])
