import streamlit as st

import pandas as pd

import numpy as np
st.set_page_config(
        page_title="PHYSICS FORMULAS AND CONSTANTS",
        page_icon="chart_with_upwards_trend",
        layout="wide",
    )
st.title(" Mechanics")
st.subheader('1. Newton’s Laws, Equations of motion and their Solutions for a Single Particle:')
st.write("1)Newton's second law of motion")
st.latex(r'''Force\left(F\right)=ma = m\frac{dv}{dt}''')
st.write("2)Angular momentum")
st.latex(r''' N = r \times p''')
st.subheader("Mechanics of system of particles")
st.subheader("Dynamics of Rigid Body")
st.subheader("Motion in a central force field")
st.subheader("Oscillations")

