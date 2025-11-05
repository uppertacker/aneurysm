import streamlit as st
import cv2
import numpy as np
from PIL import Image
import requests
import pandas as pd

st.title("Aneurysm Detection")
st.write("Please upload axial view of CT image with upto 4 optional adjacents slices") 

#Upload file
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "dcm"])
if uploaded_file:
    image = Image.open(uploaded_file)
else:
    image = Image.open(requests.get("https://picsum.photos/200/120", stream=True).raw)
agree = st.checkbox("Check here if uploaded CT image is positive for Aneurysm")

#Request
if st.button("Run Predictions"):
    res = {"isError": "false", "message": "Success", "HUpred": "78", "NORpred": "56"}
    
    #Graph
    st.write("Prediction obtained")
    df = pd.DataFrame([[float(res['HUpred']), float(res['NORpred'])]], index=['% Prediction'], columns=["HU Treatment", "Reference"])
    st.bar_chart(df, horizontal=True, stack=False)
