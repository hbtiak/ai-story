import streamlit as st
from PIL import Image
import requests
import random
from io import BytesIO
import time

st.set_page_config(page_title="Human-AI Story Illustration Lab", layout="wide")

st.title("🎨 Human–AI Co-Creative Story Illustration Tool")
st.write("Artist collaborates with AI to explore storytelling visuals.")

# -------------------------------
# INPUTS
# -------------------------------

scene = st.text_input(
    "Describe the story scene",
    "Hanuman jumping across the ocean to Lanka"
)

style = st.selectbox(
    "Choose artistic style",
    ["Comic Book", "Caricature", "Epic Painting", "Watercolor"]
)

mood = st.selectbox(
    "Mood",
    ["Heroic", "Divine", "Battle", "Sunset"]
)

exaggeration = st.slider("Character exaggeration", 1, 10, 5)

artist_image = st.file_uploader("Upload your sketch", type=["png","jpg","jpeg"])


# -------------------------------
# AI SUGGESTIONS
# -------------------------------

st.header("🤖 AI Creative Suggestions")

layouts = [
"Hero centered composition",
"Low angle dramatic perspective",
"Diagonal action layout",
"Triangular cinematic composition",
"Wide battlefield panoramic composition"
]

palette = {
"Heroic": ["Gold","Deep Red","Royal Blue"],
"Divine": ["White","Gold","Light Blue"],
"Battle": ["Black","Crimson","Dark Purple"],
"Sunset": ["Orange","Pink","Violet"]
}

col1, col2 = st.columns(2)

with col1:

    if st.button("Suggest Composition"):
        st.success(random.choice(layouts))

with col2:

    if st.button("Suggest Color Palette"):
        st.success(", ".join(palette[mood]))


# -------------------------------
# SHOW SKETCH
# -------------------------------

if artist_image:
    st.header("Artist Sketch")
    img = Image.open(artist_image)
    st.image(img, width=350)


# -------------------------------
# IMAGE GENERATION
# -------------------------------

def generate_image(prompt):

    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"

    headers = {
        "Authorization": f"Bearer {st.secrets['HF_TOKEN']}"
    }

    for _ in range(5):

        response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": prompt},
            timeout=60
        )

        # success
        if response.status_code == 200:
            return Image.open(BytesIO(response.content))

        # model loading
        if "loading" in response.text.lower():
            st.warning("Model is loading on HuggingFace... retrying")
            time.sleep(10)
            continue

        # show real error
        st.error(response.text)
        return None

    st.error("Model took too long to start")
    return None


# -------------------------------
# GENERATE SCENE
# -------------------------------

if st.button("Generate Illustration"):

    prompt = f"""
    Epic mythological illustration of {scene}.
    Style: {style}.
    Mood: {mood}.
    Character exaggeration level {exaggeration}.
    Dramatic cinematic lighting.
    Highly detailed illustration.
    """

    st.write("Prompt used by AI:")
    st.code(prompt)

    st.write("Generating illustration...")

    try:

        img = generate_image(prompt)

        if img:
            st.image(img, width=500)

        else:
            st.error("Image generation failed")

    except:
        st.error("Model loading or API error")
