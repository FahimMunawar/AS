import streamlit as st

st.set_page_config(page_title="How To", layout="centered")

st.title("How to Use This App")

st.markdown("1. **Select Image Type**: Choose the type of image you want to classify from the dropdown menu. (Axial or Coronal).📊")
st.markdown("If you have an Axial MRI scan then choose **Axial**.📊")
st.markdown("If you have an Coronal MRI scan then choose **Coronal**.📊")
st.image("step_ss/step1_image.png", caption="Step 1: Select Image Type", use_container_width=True)

# Step 2
st.markdown("2. **Upload or Drag & Drop**: Upload your image or drag and drop it into the upload area.📤")
st.image("step_ss/step2_image.png", caption="Step 2: Upload or Drag & Drop", use_container_width=True)

# Step 3
st.markdown("3. **View Results**: The classification result will be displayed instantly.🔍")
st.image("step_ss/step3_image.png", caption="Step 3: View Results", use_container_width=True)

st.markdown("---")
st.markdown("# About")
st.markdown(
    "📖This website allows you to classify medical images using a CNN model. "
    "Choose the image type, upload your image, and get instant results."
)

st.markdown("Made by Munawar")  # Replace with your personal link or profile
st.markdown("---")