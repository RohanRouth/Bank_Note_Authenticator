# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 00:05:50 2022

@author: Rohan
"""
#from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
#import flasgger
#from flasgger import Swagger
import streamlit as st


#app=Flask(__name__)
#Swagger(app)
pickle_in = open(r"C:\Users\Rohan\Desktop\Bank note Authentication\classifier.pkl",'rb')
classifier = pickle.load(pickle_in)

#@app.route("/")
def welcome():
    return "welcome all!"

#@app.route("/predict",methods=['get'])
def pred_note_authentication(variance,skewness,curtosis,entropy):
    
    """Bank note authentication
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
        
    """
    
    #variance=request.args.get("variance")
    #skewness=request.args.get("skewness")
    #curtosis=request.args.get("curtosis")
    #entropy=request.args.get("entropy")
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    return "the predicted value is " + str(prediction)

#@app.route("/predict_file",methods=["post"])
def predict_note_file():
    df_test = pd.read_csv(request.files.get("file"))
    prediction = classifier.predict(df_test)
    return "the predicted values are:" + str(list(prediction))

def main():
    st.title("Bank Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Type Here")
    skewness = st.text_input("skewness","Type Here")
    curtosis = st.text_input("curtosis","Type Here")
    entropy = st.text_input("entropy","Type Here")
    result=""
    if st.button("Predict"):
        result=pred_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")

if __name__ == "__main__":
    main()
    
    
    