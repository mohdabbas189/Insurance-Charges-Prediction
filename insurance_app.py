import streamlit as st
import numpy as np
import joblib
st.title("Inusrance Charges")
obj=joblib.load("insurance.joblib")
models=obj["model"]
cols=obj["columns"]
ln=[]
for i in cols:
    if i=="smoker":
        v=st.selectbox("Smoker",[0,1])
    
    else:
        v=st.number_input(f"enter the value of {i}")
    ln.append(v)

if st.button("click"):
    out=models.predict([ln])
    st.write(f"the charges for the insurance is {out}")
            