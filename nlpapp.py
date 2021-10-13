import streamlit as st 
import joblib
st.title('SPAM HAM CLASSIFICATION')  #title to the web app
text_model = joblib.load('spam-ham') #load the model back using joblib 
ip = st.text_input('Enter your message :')  #user input in streamlit 
op = text_model.predict([ip])           #predict if the written message is spam or ham 
if st.button('Predict'):   #creating a button called as predict
  st.title(op[0])  #gives the output in the app