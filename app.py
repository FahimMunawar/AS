import os
import keras
from keras.models import load_model
import streamlit as st 
import tensorflow as tf
import numpy as np

st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6; /* Light blue-gray */
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header('Ankylosing Spondylitis Classification CNN Model')


# model = load_model('seq_axial.h5')

option = st.selectbox(
    "What kind of image would you like to classify?",
    ("Axial", "Coronal", "Contrast"),
    index=None,
    placeholder="Select the classification method based on the type of image.",
)

# Load the appropriate model based on user selection
if option == "Axial":
    model = load_model('seq_axial.h5')
    class_names = ['Axial_AS', 'Axial_HC']
elif option == "Coronal":
    model = load_model('seq_coronal.h5')
    class_names = ['Coronal_AS', 'Coronal_HC']
elif option == "Contrast":
    model = load_model('seq_contrast.h5')
    class_names = ['Control_Enhanced_AS', 'Control_Enhanced_HC']

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array,0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = 'The Image belongs to ' + class_names[np.argmax(result)] + ' with a score of '+ str(np.max(result)*100)
    return outcome

uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, width = 200)

    st.markdown(classify_images(uploaded_file))

st.snow()