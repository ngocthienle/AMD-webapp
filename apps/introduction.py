# -*- coding: utf-8 -*-
"""
Created on Tuesday, October 24 07:43:53 2023
This is the Deep Learning web application for eye disease diagnosis.
@author: thienle
"""
import streamlit as st
from PIL import Image

def app():
    image = Image.open('eye_logo.png')
    st.image(image)

    st.title("""Development and Implementation of Web Application Platform for Eye Disease Diagnosis using Artificial Intelligence""")
    st.write(" ------ ")
    st.subheader("""Goals""")
    st.write("- AI model-based Webapp to classify fundus image into normal,dry AMD,and wet AMD disease.")
    st.write("- Based on the diagnosis results given by proposed model, the ophthalmologist then has suitable treatment plan for the patient and can follow up duration.")
    st.write("- Minimize the unnecessary visit for the patient which helps to improve the health care facility and reduce an indirect burden cost loss for the patient.")
    
    expander_faq = st.expander("More About The Project")
    expander_faq.write("Thank you for visiting! If you have any questions about our project, please contact:")
    expander_faq.write("Professor Dr. Watit Benjapolakul: watit.b@chula.ac.th")

    
    
    
    