import streamlit as st
import pickle
import numpy as np

today = [25,27,0.22,2.3,12.5,34,11,13,66.0,66.0,1020.0,1001.0,3.4,9.0,26.0,22.0,1,1.2]

# o = [257,277,0.227,7.3,122.5,341,1134,1334,6611.130,466.0,123020.0,13001.0,32.4,923.0,2346.0,22.0,1,1.2]

st.write(
    '''
# Weather Predictor
'''
)
clf = pickle.load(open("clf.pkl",'rb'))

values = st.text_input("Enter comma separated values")
vals = values.split(",")





if st.button("Submit") == True:
     output = clf.predict([vals])
     if int(output[0]) == 0:
       st.write("""### Accoding to the Machine Learning Model Tomorrow will be no `RAIN`""")
     else:
       st.write("""### Accoding to the Machine Learning Model Tomorrow will be `RAIN`""")

