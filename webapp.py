import streamlit as st
st.title("Itis Prediction")
import pickle
model =pockle.load(open("model_iris.pkl","rb"))
SL=st.slidet("SL",2.0,10.0)
sw=st.slidet("sw",2.0,10.0)
PL=st.slidet("PL",2.0,10.0)
PW=st.slidet("PW",2.0,10.0)
if st.button("Predict"):
 st. success model. predict([[sl, sw, pl, pw]]))
