import requests
import io
import streamlit as st
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input("Enter Your Thoughts"),
})
# You can access the image with PIL.Image for example
image = Image.open(io.BytesIO(image_bytes))

# Create a Streamlit application
#st.title('Display Image Example')
st.image(image, caption='Sample Image')