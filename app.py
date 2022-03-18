import streamlit as st
import pickle 

pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

def prediction(wheel, carlen, carwid , carheight, curbweight,eng_size, bore_ratio, stroke,compratio,hp, prpm):  
    prediction = classifier.predict(
        [[wheel, carlen, carwid , carheight, curbweight,eng_size, bore_ratio, stroke,compratio,hp, prpm ]])
    print(prediction)
    return prediction


st.markdown("<h1 style='text-align: center'> Car Price Predictor </h1>", unsafe_allow_html=True)
st.write("""
## Predict your Car's Price : 
""")
wheel = st.text_input("Enter Car WheelBase : ")
carlen = st.text_input("Enter Car Length : ")
carwid = st.text_input("Enter Car Width : ")
carheight = st.text_input("Enter Car Height : ")
curbweight= st.text_input("Enter Curb Weight : ")
eng_size = st.text_input("Enter Engine Size : ")
bore_ratio = st.text_input("Enter Bore Ratio : ")
stroke = st.text_input("Enter Stroke : ")
compratio = st.text_input("Enter Compression Ratio : ")
hp = st.text_input("Enter Horse Power : ")
prpm = st.text_input("Enter Peak RPM : ")
result =""

_, _, _, col, _, _, _ = st.columns([1]*6+[1.18])
if col.button(' PREDICT '):
    result = prediction(wheel, carlen, carwid , carheight, curbweight,eng_size, bore_ratio, stroke,compratio,hp, prpm)
    st.success('Your Car Price is {}'.format(result))