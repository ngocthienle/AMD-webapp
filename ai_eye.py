# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 11:32:36 2021
The multi-page web application for stroke project- Chula
@author: Ngoc Thien Le, Postdoc Researcher
"""
import streamlit as st
from PIL import Image

logo_image = Image.open('logo.png')

st.set_page_config(layout="centered", page_title='AI Eyecare',
                   page_icon=logo_image)

from multiapp import MultiApp
from apps import introduction, fundus_detection  # Import the app modules want here.

app = MultiApp()

# Add all your application here
app.add_app("Project Objectives", introduction.app)
app.add_app("AMD examination", fundus_detection.app)

# The main apps
app.run()
