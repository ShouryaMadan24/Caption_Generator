import streamlit as st
st.set_page_config(page_title="Instagram Caption Assistant", layout="centered")
from PIL import Image
from image_desc import generate_image_caption
from caption_generator import generate_captions
from hashtag import suggest_hashtags

st.markdown("""
    <style>
    .stFileUploader {
        font-size: 18px !important;
    }
    .stMarkdown h1 {
        font-size: 34px !important;
    }
    .stMarkdown h2 {
        font-size: 32px !important;
    }
    .stMarkdown h3 {
        font-size: 30px !important;
    }
    .stMarkdown p {
        font-size: 20px !important;
    }
    .generated-captions span {
        font-size: 20px !important;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📸 Instagram Caption Generator")

uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Generate Captions and Hashtags"):
        with st.spinner("Analyzing image and generating captions..."):
            image_desc = generate_image_caption(image)
            captions = generate_captions(image_desc)
            hashtags = suggest_hashtags(image_desc)

        st.subheader("📝 Auto-generated Description")
        st.write(image_desc)

        st.subheader("✨ Captions")
        for i, cap in enumerate(captions, 1):
            st.markdown(f'<div class="generated-captions" style="margin-bottom: 20px;"><span>{i}. {cap}</span></div>', unsafe_allow_html=True)

        st.subheader("🔥 Hashtags")
        st.write(" ".join(hashtags))