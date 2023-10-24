# -*- coding: utf-8 -*-
"""
Created on Tuesday, October 24 07:43:53 2023
This is the Deep Learning web application for eye disease diagnosis.
@author: thienle
"""
import cv2
import numpy as np
# Import libraries
import streamlit as st
import tensorflow as tf
from PIL import Image
from tensorflow.keras.applications.inception_v3 import preprocess_input as v3_preprocess_input


@st.cache_resource(experimental_allow_widgets=True)
def load_model():
    model = tf.keras.models.load_model(
        "aimodels/classification_AMD_Classification_InceptionV3.hdf5"
    )

    return model


with  st.spinner('Loading Model Into Memory...'):
    model = load_model()


def app():
    image = Image.open('eye_logo.png')
    st.image(image)
    st.title("""Age-Related Macular Degeneration (AMD) Examination""")
    # Create header explaination
    my_expander = st.expander("See explanation", expanded=False)
    with my_expander:
        st.write("""
                 This AI based- webapp examines a fundus image as Normal, Wet AMD, or Dry AMD using backend AI engine.
                 The trained AI engine is based on the Vision Transformer (ViT) deep learning model.
                     """)
        image = Image.open('example_fundus.png')
        st.image(image,
                 caption='Example AMD classification.')

    st.subheader('Upload a fundus image and obtain the examination by AI model')
    uploaded_file = st.file_uploader("Upload fundus image")

    map_dict = {1: 'Dry AMD.',
                2: 'Normal.',  # 
                0: 'Wet AMD.',  # 
                }
    if uploaded_file is not None:
        # Convert the file to an opencv image.
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)
        opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(opencv_image, (224, 224))
        # Now do something with the image! For example, let's display it:
        st.image(opencv_image, channels="RGB", use_column_width=False, width=300)
        # If the trained AI model using normalized divide (/255) images, then the images for predicting also divide 255.
        resized = v3_preprocess_input(resized)  # Normalized the input images by divide 255.
        img_reshape = resized[np.newaxis, ...]

        Genrate_pred = st.button("Examine this image")
        if Genrate_pred:
            prediction = model.predict(img_reshape).argmax()
            if prediction == 0: st.error("The retina is {}".format(map_dict[prediction]))
            if prediction == 1: st.error("The retina is {}".format(map_dict[prediction]))
            if prediction == 2: st.info("The retina is {}".format(map_dict[prediction]))
