from PIL import Image
import streamlit as st

st.title("Applicant Data")

st.text_input("Name", placeholder="Jon Doe")
st.number_input("Age", min_value=20,max_value=30)
st.text_input("State", placeholder="Idaho")
st.number_input("Height", min_value=150,max_value=180, step=3)
st.radio("Gender",["Male","Female"])
st.sidebar.selectbox("Country",["Nigeria","Ghana","Uganda","Cameroun"])
st.multiselect("Education",["WAEC","BSC","pHD","MSc"])

if st.sidebar.checkbox("Agree"):
   st.sidebar.write("Permission Granted")
else:
   st.sidebar.warning("Click Agree")

   if st.button("Application"):
      st.success("Application Successful")
      st.balloons()





