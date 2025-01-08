import os
import tensorflow as tf
import numpy as np
import streamlit as st
from keras.models import load_model

st.set_page_config(page_title="Image Classification", layout="wide")

# Particles.js HTML template for full-screen background
particles_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Particles Background</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            overflow: hidden;
        }
        #particles-js {
            position: fixed;
            width: 100vw;
            height: 100vh;
            top: 0;
            left: 0;
            z-index: -1; /* Send particles to the background */
        }
        .content {
            position: relative;
            z-index: 1; /* Content stays on top of particles */
            color: white; /* Ensure text is visible */
            text-align: center;
            padding-top: 50px; /* Adjust the space from the top */
        }
        .content h1, .content p {
            margin: 20px 0;
        }
    </style>
</head>
<body>
    <div id="particles-js"></div>
    <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
    <script>
        particlesJS("particles-js", {
            "particles": {
                "number": {
                    "value": 150,
                    "density": {
                        "enable": true,
                        "value_area": 800
                    }
                },
                "color": {
                    "value": "#ffffff"
                },
                "shape": {
                    "type": "circle",
                    "stroke": {
                        "width": 0,
                        "color": "#000000"
                    }
                },
                "opacity": {
                    "value": 0.5,
                    "random": true
                },
                "size": {
                    "value": 3,
                    "random": true
                },
                "line_linked": {
                    "enable": true,
                    "distance": 150,
                    "color": "#ffffff",
                    "opacity": 0.4,
                    "width": 1
                },
                "move": {
                    "enable": true,
                    "speed": 2,
                    "direction": "none",
                    "random": false,
                    "straight": false,
                    "out_mode": "out",
                    "bounce": false
                }
            },
            "interactivity": {
                "detect_on": "canvas",
                "events": {
                    "onhover": {
                        "enable": true,
                        "mode": "grab"
                    },
                    "onclick": {
                        "enable": true,
                        "mode": "push"
                    }
                },
                "modes": {
                    "grab": {
                        "distance": 140,
                        "line_linked": {
                            "opacity": 1
                        }
                    },
                    "push": {
                        "particles_nb": 4
                    }
                }
            },
            "retina_detect": true
        });
    </script>
</body>
</html>
"""

# Render Particles.js as a full-screen background
st.components.v1.html(particles_html, height=100, width=2000)

# Streamlit app content
st.markdown("""
    <div class="content">
        <h1>Ankylosing Spondylitis Classification!</h1>
        <p>This is an  app that classfies whether your MRI images represent Ankylosing Spondylitis or Healthy MRI's.</p>
        <h3>Class Descriptions:</h3>
        <ul style="text-align:left; font-size: 18px;">
            <li><strong>Axial_AS</strong>: Axial MRI with Ankylosing Spondylitis</li>
            <li><strong>Axial_HC</strong>: Axial MRI Healthy</li>
            <li><strong>Coronal_AS</strong>: Coronal MRI with Ankylosing Spondylitis</li>
            <li><strong>Coronal_HC</strong>: Coronal MRI Healthy</li>
            <li><strong>Contrast_AS</strong>: Contrast MRI with Ankylosing Spondylitis</li>
            <li><strong>Contrast_HC</strong>: Contrast MRI Healthy</li>
        </ul>
    </div>
""", unsafe_allow_html=True)
# Image classification section
st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical spacing

# Select box for image classification
option = st.selectbox(
    "What kind of image would you like to classify?",
    ("Axial", "Coronal","Contrast"),
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
    class_names = ['Contrast_AS', 'Contrast_HC']

def classify_images(image_path):
    input_image = tf.keras.utils.load_img(image_path, target_size=(180,180))
    input_image_array = tf.keras.utils.img_to_array(input_image)
    input_image_exp_dim = tf.expand_dims(input_image_array,0)

    predictions = model.predict(input_image_exp_dim)
    result = tf.nn.softmax(predictions[0])
    outcome = f"\n\n{'*' * 50}\nThe Image belongs to {class_names[np.argmax(result)]} with a score of {np.max(result) * 100:.2f}%\n{'*' * 50}\n\n"
    return outcome

# File uploader for image
uploaded_file = st.file_uploader('Upload an Image')
if uploaded_file is not None:
    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds vertical spacing
    with open(os.path.join('upload', uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer())
    
    st.image(uploaded_file, width=800)

    st.markdown(classify_images(uploaded_file))

st.components.v1.html(particles_html, height=300, width=2000)


