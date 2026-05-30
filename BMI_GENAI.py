import streamlit as st
import google.genai as genai

client = genai.Client(api_key="AIzaSyCRsvYFMK9Ym4ry1ath0OHFQoau949rf3w")

st.title("BMI Calculator with AI Nutritionist")

name= st.text_input("Enter your name")
ht= st.slider("Enter your height in meters : ", min_value = 1.0,max_value=2.5, step = 0.01)
wt= st.slider("Enter your weight in kgs : ", min_value = 1.0,max_value = 150.0 ,step = 0.01)
gender = st.selectbox("select your gender : ",["male", "female"])

BMI = wt/(ht**2)
st.write(f"Your BMI is :{BMI: .2f}")
prompt = f"Act like an expert nutritionist,comment on the BMI with the following result"

response = client.models.generate_content(model="gemini-2.5-flash",contents=prompt)

st.write(response.text)