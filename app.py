import streamlit as st
import pickle

#model=pickle.load(open("model.pkl",'rb'))

with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

st.markdown("streamlit is cool")
st.title("fail/pass classifier streamlit app")
study_hour=st.number_input("Enter study hours 1 to 10",min_value=1,max_value=10,)
play_hour=st.number_input("Enter playing hours 1 to 10",min_value=1,max_value=10,)
# st.button("submit",1,"click to submit the request",)
if st.button("submit"):
    result=model.predict([[study_hour,play_hour]])
    if result==1:

        st.write("pass")
    else:
        st.write("fail")
