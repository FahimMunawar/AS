import streamlit as st
import os

st.set_page_config(page_title="Sample Images", layout="centered")

st.title("Sample Images")

# Dropdown to select the image category
option = st.selectbox(
    "Choose a category to view sample images:",
    [
        "Axial AS", "Axial HC", 
        "Coronal AS", "Coronal HC", 
        "Contrast AS", "Contrast HC"
    ]
)

# Define the path to the sample images folder
sample_folder = "Sample"

# Function to display images from a given folder
def display_images(folder_path):
    images = os.listdir(folder_path)
    for image in images:
        image_path = os.path.join(folder_path, image)
        st.image(image_path, caption=image, use_container_width=True)

if option == "Axial AS":
    st.subheader("Axial AS (Axial MRI with Ankylosing Spondylitis)")
    display_images(os.path.join(sample_folder, "Axial_AS"))

elif option == "Axial HC":
    st.subheader("Axial HC (Axial MRI Healthy)")
    display_images(os.path.join(sample_folder, "Axial_HC"))

elif option == "Coronal AS":
    st.subheader("Coronal AS (Coronal MRI with Ankylosing Spondylitis)")
    display_images(os.path.join(sample_folder, "Coronal_AS"))

elif option == "Coronal HC":
    st.subheader("Coronal HC (Coronal MRI Healthy)")
    display_images(os.path.join(sample_folder, "Coronal_HC"))

elif option == "Contrast AS":
    st.subheader("Contrast AS (Contrast MRI with Ankylosing Spondylitis)")
    display_images(os.path.join(sample_folder, "Contrast_AS"))

elif option == "Contrast HC":
    st.subheader("Contrast HC (Contrast MRI Healthy)")
    display_images(os.path.join(sample_folder, "Contrast_HC"))
