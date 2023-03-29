import streamlit as st 
from PIL import Image


st.title("This is My WPI Calculator")

img = Image.open("bmi.jpg")
st.image(img)

# Introduction

st.subheader("Introduction")

st.text("""
Calculation of proposed water pollution index (WPI)

For this purpose, water quality parameters viz., TDS and Turbidity, were
Collected for 4 years (2016-2019) from 3 sampling stations (1,2,and3)
along Shatt Al-Arab River, southern part of Iraq, in Basrah city.

However, WPI can accommodate more number of variables as it is flexible for n
number of parameters.  (here , Tur, and TDS are most effective parameters).


Obesity is frequently subdivided into categories:

Class 1:   < 0.5            Excellent water
Class 2:   0.5−0.75      Good wate
Class 3:   0.75−1        Moderately polluted water
Class 4:   > 1              Highly polluted water

Reff.: Hossain, M., & Patra, P. K. (2020). Water pollution index–
A new integrated approach to rank water quality. Ecological Indicators, 117, 106668.

	""")


# Input

tds = st.number_input("Enter TDS in mg/l")

tur = st.number_input("Enter Turbidity in Ntu")


wpi = (tds+237*((tur)**0.5))/1675

st.success(f"The WPI is {wpi}")
