import streamlit as st

st.set_page_config(page_title="BMI Calculator", page_icon="😃", layout="centered")
st.title("Project 9: BMI Calculator In Python")
st.markdown("""
## Apna Body Mass Index (BMI) calculator karein  
Nechay **weight and height** enter karein:
""")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Height (m)", min_value=1.0, format="%.2f")  # Fixed min_value and format

if height > 0 and weight > 0:  # Fixed colon
    bmi = weight / (height ** 2)  # Fixed exponentiation
    st.subheader("Apka BMI Hai:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)  # Fixed f-string

    if bmi < 18.5:
        st.error("Underweight")
    elif 18.5 <= bmi < 24.9:
        st.success("Normal Weight")
    elif 25 <= bmi < 29.9:
        st.warning("Overweight")
    else:
        st.error("Obesity")
else:
    st.info("Please enter valid weight and height.")
