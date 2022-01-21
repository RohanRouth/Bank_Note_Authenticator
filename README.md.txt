# Dockerize and deploy machine learning model using Flask,Flasgger and Streamlit
Two simple  applications that can autheticate banks notes based on features such as variance,skewness,curtosis and entropy using Random forest.


# Instructions
A.Flask app
1. pip install -r requirements.txt
2. Run Flask_app from app folder
3. Web application will start Running on http://127.0.0.1:5000/apidocs/

B.streamlit app
1. pip install -r requirements.txt
2. On terminal  go to App directory and use command streamlit run streamlit_app.py
3. web app will open automatically in web browser.

#project description
Data were extracted from images that were taken from genuine and forged banknote-like specimens.
For digitization, an industrial camera usually used for print inspection was used.
The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained.
Wavelet Transform tool were used to extract features from images.
I built a simple Random forest model to classify fake notes and deployed it by creating web applications using flask,flasgger and streamlit.


Flask app - 

>![](images/flask app.png)

flask app output-


>![](images/flask app output.png)

streamlit app-


>![](images/streamlit app.png)




